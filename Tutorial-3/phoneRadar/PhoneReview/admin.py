from django.contrib import admin
from .models import Brand, PhoneModel, Review, ReviewResource


# Brand Admin
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin_country', 'manufacturing_since', 'created_at')
    list_filter = ('origin_country', 'created_at')
    search_fields = ('name', 'origin_country')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'origin_country', 'manufacturing_since')
        }),
        ('Additional Details', {
            'fields': ('website_url', 'description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Phone Model Admin
@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'platform', 'launch_date', 'created_at')
    list_filter = ('brand', 'platform', 'launch_date')
    search_fields = ('model_name', 'brand__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Model Information', {
            'fields': ('brand', 'model_name', 'platform', 'launch_date')
        }),
        ('Specifications', {
            'fields': ('storage_options', 'specifications', 'description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Review Resource Inline Admin
class ReviewResourceInline(admin.TabularInline):
    model = ReviewResource
    extra = 1
    fields = ('title', 'url', 'description')


# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'date_published', 'is_active')
    list_filter = ('rating', 'date_published', 'is_active', 'phone_models__brand')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('date_published', 'updated_at')
    filter_horizontal = ('phone_models',)
    inlines = [ReviewResourceInline]
    fieldsets = (
        ('Review Information', {
            'fields': ('title', 'content', 'rating', 'author')
        }),
        ('Phone Models', {
            'fields': ('phone_models',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('date_published', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        # Auto-set author to current user if not already set
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


# Review Resource Admin
@admin.register(ReviewResource)
class ReviewResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'review', 'created_at')
    list_filter = ('created_at', 'review')
    search_fields = ('title', 'review__title', 'url')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Resource Information', {
            'fields': ('review', 'title', 'url', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
