from django.shortcuts import render
from .models import Products

def home(request):
    return render(request, 'products/home.html')


def products(request):
    products = Products.objects.all()
    context ={'products': products}
    return render(request, 'products/products.html', context)
