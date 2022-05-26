from django.shortcuts import render
from .models import product


# Create your views here.
def home(request):
    return render(request, 'products/home.html')


def products(request):
    Products=product.ojects.all()
    context={'Products':Products}
    return render(request, 'products/products.html',context)
