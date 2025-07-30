from django import forms
from .models import TributeMessage, PrePlanSubmission, ContactMessage


class TributeMessageForm(forms.ModelForm):
    class Meta:
        model = TributeMessage
        fields = ['author_name', 'message']
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control materialize-textarea',
                'placeholder': 'Share your memories and thoughts...',
                'rows': 4
            }),
        }


class PrePlanSubmissionForm(forms.ModelForm):
    class Meta:
        model = PrePlanSubmission
        fields = ['full_name', 'email', 'phone', 'service_type', 'venue_preference', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name of deceased'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number'
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control browser-default'
            }),
            'venue_preference': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preferred venue or location'
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control materialize-textarea',
                'placeholder': 'Any special requests or requirements...',
                'rows': 4
            }),
        }


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number (optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject of your message'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control materialize-textarea',
                'placeholder': 'Your message...',
                'rows': 5
            }),
        }


class FarewellCalculatorForm(forms.Form):
    SERVICE_CHOICES = [
        ('basic', 'Basic Service'),
        ('standard', 'Standard Service'),
        ('premium', 'Premium Service'),
    ]
    
    VENUE_CHOICES = [
        ('chapel', 'Chapel Service'),
        ('church', 'Church Service'),
        ('graveside', 'Graveside Service'),
        ('home', 'Home Service'),
    ]
    
    service_package = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control browser-default'})
    )
    venue_type = forms.ChoiceField(
        choices=VENUE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control browser-default'})
    )
    flowers = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'})
    )
    music = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'})
    )
    catering = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'})
    )
    transportation = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'})
    )
    
    def calculate_total(self):
        """Calculate the total cost based on selections"""
        base_prices = {
            'basic': 2500,
            'standard': 4000,
            'premium': 6500,
        }
        
        venue_costs = {
            'chapel': 300,
            'church': 500,
            'graveside': 200,
            'home': 150,
        }
        
        extra_costs = {
            'flowers': 200,
            'music': 300,
            'catering': 800,
            'transportation': 400,
        }
        
        total = base_prices.get(self.cleaned_data.get('service_package', 'basic'), 2500)
        total += venue_costs.get(self.cleaned_data.get('venue_type', 'chapel'), 300)
        
        if self.cleaned_data.get('flowers'):
            total += extra_costs['flowers']
        if self.cleaned_data.get('music'):
            total += extra_costs['music']
        if self.cleaned_data.get('catering'):
            total += extra_costs['catering']
        if self.cleaned_data.get('transportation'):
            total += extra_costs['transportation']
            
        return total
