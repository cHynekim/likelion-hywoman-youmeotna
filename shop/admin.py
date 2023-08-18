from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available_display', 'available_order', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['price', 'stock', 'available_display', 'available_order']

admin.site.register(Product, ProductAdmin)