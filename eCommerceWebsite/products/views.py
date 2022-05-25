from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,'products/home.html')

def products(request):
    product = Product.objects.all()
    context = {"product":product}

    return render(request,'products/products.html',context)
