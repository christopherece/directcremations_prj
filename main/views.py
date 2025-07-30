from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Obituary, TributeMessage, ServicePackage, Testimonial
from .forms import TributeMessageForm, PrePlanSubmissionForm, ContactMessageForm, FarewellCalculatorForm


def home(request):
    """Homepage with hero section, action boxes, and testimonials"""
    featured_testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    recent_obituaries = Obituary.objects.all()[:3]
    
    context = {
        'testimonials': featured_testimonials,
        'recent_obituaries': recent_obituaries,
    }
    return render(request, 'main/home.html', context)


def obituaries(request):
    """Obituaries listing page with search and pagination"""
    obituaries_list = Obituary.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        obituaries_list = obituaries_list.filter(
            Q(full_name__icontains=search_query) |
            Q(biography__icontains=search_query)
        )
    
    # Date filtering
    year = request.GET.get('year')
    month = request.GET.get('month')
    if year:
        obituaries_list = obituaries_list.filter(date_of_death__year=year)
    if month:
        obituaries_list = obituaries_list.filter(date_of_death__month=month)
    
    # Pagination
    paginator = Paginator(obituaries_list, 6)  # Show 6 obituaries per page
    page_number = request.GET.get('page')
    obituaries = paginator.get_page(page_number)
    
    context = {
        'obituaries': obituaries,
        'search_query': search_query,
        'year': year,
        'month': month,
    }
    return render(request, 'main/obituaries.html', context)


def obituary_detail(request, pk):
    """Individual obituary page with tribute messages"""
    obituary = get_object_or_404(Obituary, pk=pk)
    approved_tributes = obituary.tributes.filter(approved=True)
    
    if request.method == 'POST':
        form = TributeMessageForm(request.POST)
        if form.is_valid():
            tribute = form.save(commit=False)
            tribute.obituary = obituary
            tribute.save()
            messages.success(request, 'Your tribute has been submitted and is awaiting approval.')
            return redirect('obituary_detail', pk=pk)
    else:
        form = TributeMessageForm()
    
    context = {
        'obituary': obituary,
        'tributes': approved_tributes,
        'form': form,
    }
    return render(request, 'main/obituary_detail.html', context)


def funeral_planning(request):
    """Funeral planning guides and information"""
    return render(request, 'main/funeral_planning.html')


def arrange_service(request):
    """Service arrangement form"""
    if request.method == 'POST':
        form = PrePlanSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            
            # Send email notification (in production, configure proper email settings)
            try:
                send_mail(
                    'New Service Arrangement Request',
                    f'New service arrangement from {submission.full_name}. '
                    f'Service type: {submission.service_type}. '
                    f'Contact: {submission.email}, {submission.phone}',
                    settings.DEFAULT_FROM_EMAIL,
                    ['admin@funeralservices.com'],  # Replace with actual admin email
                    fail_silently=True,
                )
            except Exception:
                pass  # Email sending failed, but form submission succeeded
            
            messages.success(request, 'Your service arrangement request has been submitted. We will contact you soon.')
            return redirect('arrange_service')
    else:
        form = PrePlanSubmissionForm()
    
    context = {'form': form}
    return render(request, 'main/arrange_service.html', context)


def farewell_calculator(request):
    """Farewell cost calculator"""
    total_cost = None
    
    if request.method == 'POST':
        form = FarewellCalculatorForm(request.POST)
        if form.is_valid():
            total_cost = form.calculate_total()
    else:
        form = FarewellCalculatorForm()
    
    context = {
        'form': form,
        'total_cost': total_cost,
    }
    return render(request, 'main/farewell_calculator.html', context)


def contact(request):
    """Contact page with form and information"""
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactMessageForm()
    
    context = {'form': form}
    return render(request, 'main/contact.html', context)


def about(request):
    """About page"""
    return render(request, 'main/about.html')


def our_approach(request):
    """Our approach page"""
    return render(request, 'main/our_approach.html')
