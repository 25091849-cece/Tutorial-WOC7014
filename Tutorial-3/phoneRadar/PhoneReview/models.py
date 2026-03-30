from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Brand Model - Stores information about phone brands/manufacturers
class Brand(models.Model):
    """Model to store phone brand information"""
    name = models.CharField(max_length=100, unique=True)
    origin_country = models.CharField(max_length=100)
    manufacturing_since = models.IntegerField(validators=[MinValueValidator(1900)])
    website_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Phone Model - Stores information about specific phone models
class PhoneModel(models.Model):
    """Model to store phone model information"""
    PLATFORM_CHOICES = [
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Windows', 'Windows Phone'),
        ('Other', 'Other'),
    ]
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phone_models')
    model_name = models.CharField(max_length=200)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    storage_options = models.CharField(max_length=200, help_text="e.g., 128GB, 256GB, 512GB")
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True, help_text="Additional specs and features")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"

    class Meta:
        ordering = ['-launch_date']
        unique_together = ['brand', 'model_name']


# Review Model - Stores phone review articles
class Review(models.Model):
    """Model to store phone reviews"""
    title = models.CharField(max_length=300)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    phone_models = models.ManyToManyField(PhoneModel, related_name='reviews')
    date_published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"

    class Meta:
        ordering = ['-date_published']


# Resource/Link Model - Stores related resources/links for reviews
class ReviewResource(models.Model):
    """Model to store links/resources related to reviews"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.review.title}"

    class Meta:
        ordering = ['-created_at']
