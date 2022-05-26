from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='base'),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),

]