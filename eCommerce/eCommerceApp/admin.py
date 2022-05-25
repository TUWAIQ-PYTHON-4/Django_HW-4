from django.contrib import admin
from .models import *

class SellerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    date_hierarchy = 'registration_date'

class ProductAdmin(admin.ModelAdmin):
     list_display = ('name', 'quantity')
     list_filter = ('seller', 'quantity')
     date_hierarchy = 'registration_date'
     search_fields = ['name']

# Register your models here.
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
