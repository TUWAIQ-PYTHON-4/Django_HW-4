from django.urls import path
from numpy import product
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('products', views.products, name='products')
]