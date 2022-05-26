from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the products.")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="The creation time of the products.")
    price = models.IntegerField(null=True, help_text="The price of the products.")
    product_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name,


class Seller(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the seller.")
    description = models.TextField(help_text="The description about the seller.")
    Products = models.ForeignKey('Products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
