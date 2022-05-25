from django.contrib import admin
from .models import Seller,Product

'''class SellerAdmin(admin.ModelAdmin):
    list_display = ('name',)'''

admin.site.register(Product)
admin.site.register(Seller)
