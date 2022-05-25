from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'products/products.html')


def products (request):
    return render(request,'products/products.html')