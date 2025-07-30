from django.contrib import admin
from .models import (
    Obituary, TributeMessage, ServicePackage, ServiceExtra,
    PrePlanSubmission, ContactMessage, Testimonial
)


@admin.register(Obituary)
class ObituaryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'date_of_birth', 'date_of_death', 'service_location', 'service_datetime']
    list_filter = ['date_of_death', 'service_location', 'created_at']
    search_fields = ['full_name', 'biography']
    date_hierarchy = 'date_of_death'
    readonly_fields = ['created_at']


@admin.register(TributeMessage)
class TributeMessageAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'obituary', 'approved', 'created_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['author_name', 'message', 'obituary__full_name']
    actions = ['approve_tributes', 'unapprove_tributes']
    
    def approve_tributes(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} tributes approved.")
    approve_tributes.short_description = "Approve selected tributes"
    
    def unapprove_tributes(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f"{queryset.count()} tributes unapproved.")
    unapprove_tributes.short_description = "Unapprove selected tributes"


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'base_price', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']


@admin.register(ServiceExtra)
class ServiceExtraAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']


@admin.register(PrePlanSubmission)
class PrePlanSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'service_type', 'submitted_at', 'is_processed']
    list_filter = ['service_type', 'is_processed', 'submitted_at']
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['submitted_at']
    actions = ['mark_as_processed']
    
    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
        self.message_user(request, f"{queryset.count()} submissions marked as processed.")
    mark_as_processed.short_description = "Mark selected submissions as processed"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['submitted_at']
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured', 'created_at']
    search_fields = ['author_name', 'content']
    actions = ['feature_testimonials', 'unfeature_testimonials']
    
    def feature_testimonials(self, request, queryset):
        queryset.update(is_featured=True)
        self.message_user(request, f"{queryset.count()} testimonials featured.")
    feature_testimonials.short_description = "Feature selected testimonials"
    
    def unfeature_testimonials(self, request, queryset):
        queryset.update(is_featured=False)
        self.message_user(request, f"{queryset.count()} testimonials unfeatured.")
    unfeature_testimonials.short_description = "Unfeature selected testimonials"


# Customize admin site header
admin.site.site_header = "Funeral Services Admin"
admin.site.site_title = "Funeral Services"
admin.site.index_title = "Welcome to Funeral Services Administration"
