from django.db import models
from django.utils import timezone


class Obituary(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    biography = models.TextField(blank=True)
    service_location = models.CharField(max_length=255)
    service_datetime = models.DateTimeField()
    photo = models.ImageField(upload_to='obituaries/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_of_death']
        verbose_name_plural = "Obituaries"

    def __str__(self):
        return self.full_name


class TributeMessage(models.Model):
    obituary = models.ForeignKey(Obituary, related_name='tributes', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Tribute from {self.author_name} for {self.obituary.full_name}"


class ServicePackage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['base_price']

    def __str__(self):
        return self.title


class ServiceExtra(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PrePlanSubmission(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('burial', 'Burial'),
        ('cremation', 'Cremation'),
    ]
    
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    venue_preference = models.CharField(max_length=255, blank=True)
    special_requests = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Pre-plan submission from {self.full_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial from {self.author_name}"
