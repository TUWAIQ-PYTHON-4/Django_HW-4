from django.db import models



class Seller(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    profile = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='seller/photos/')
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photo/')
    def __str__(self):
        return self.name
