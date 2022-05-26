from django.shortcuts import render
from .models import Products

# Create your views here.
def home (request):
    return render(request,'products/home.html')


def products (request):
    products = Products.objects.all()
    paginator = paginator(products , 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {'products':paged_products}
    return render(request,'products/products.html' ,context )