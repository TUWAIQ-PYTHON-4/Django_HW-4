from django.shortcuts import render
from . import models #models

# Create your views here.
def shop(request):
    context_product = models.Product.objects.all()# models
    return render(request, 'shop.html', {'context_product': context_product})# templets


