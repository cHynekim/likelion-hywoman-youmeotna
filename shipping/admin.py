from django.contrib import admin
from .models import Shipping, DeliveryBundle

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_product_names', 'status', 'delivery_date')
    list_filter = ('status', 'delivery_date')

    def get_product_names(self, obj):
        return ", ".join(str(product) for product in obj.products.all())
    get_product_names.short_description = 'Products'

# Register your models here.
admin.site.register(Shipping, ShippingAdmin)

