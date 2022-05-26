from django.contrib import admin

from django.contrib import admin

from .models import products
class productsAdmin(admin.ModelAdmin):
    list_display = ['namep']

admin.site.register(products,productsAdmin)

from .models import seller


class sellerAdmin(admin.ModelAdmin):
    list_filter = ['name']
admin.site.register(seller, sellerAdmin)