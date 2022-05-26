from django.db import models


# Create your models here.

class seller(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seller = models.ForeignKey(seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='prodect/photos/')

    def __str__(self):
        return self.name
