from django.db import models

# Create your models here.
class Seller(models.Model):
    first_name = models.CharField(max_length = 25, help_text = 'this is the seller first name')
    last_name = models.CharField(max_length = 25, help_text = 'this is the seller last name')
    email = models.EmailField(help_text = 'this is the seller email')
    registration_date = models.DateTimeField(auto_now_add=True, help_text='this is seller registration_date')
    seller_profile_pic = models.ImageField(upload_to='sellers_profile_pic')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    name = models.CharField(max_length = 25, help_text = 'this the prodect name')
    description = models.TextField(help_text = 'this a prodect discription')
    quantity = models.IntegerField(help_text = 'this the prodect amount')
    registration_date = models.DateTimeField(auto_now_add=True, help_text='this is seller registration_date')
    product_img = models.ImageField(upload_to='products_img')

    def __str__(self):
        return f'{self.name} {self.quantity}'

