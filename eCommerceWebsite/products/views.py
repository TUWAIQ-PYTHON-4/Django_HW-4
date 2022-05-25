from django.shortcuts import render
from .models import Product
def home(request):
    return render(request,'home.html')

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'products.html',context)
# Create your views here.
