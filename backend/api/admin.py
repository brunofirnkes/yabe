from django.contrib import admin
from .models import *

class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    inlines = [ProductReviewInline]

admin.site.register(Product, ProductAdmin)