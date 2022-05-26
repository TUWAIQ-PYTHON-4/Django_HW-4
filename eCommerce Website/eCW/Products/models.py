from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Seller(models.Model):
    name=models.CharField(max_length=50 , help_text="Task Title")
    phone =models.CharField(max_length=20)
    email=models.TextField(max_length=50)
    profile= models.TextField(blank=True)
    photo=models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200, help_text="The name of project ")
    description = models.TextField(blank=True)
    price = models.IntegerField (help_text="The price " )
    seller = models.ForeignKey(Seller,on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photos/')


    def __str__(self):
        return self.name



