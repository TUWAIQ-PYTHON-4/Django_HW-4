from django.db import models

# Create your models here.
class seller(models.Model):
    seller_name = models.CharField(max_length=100, help_text="seller name")


    def __str__(self):
        return self.seller_name

class product(models.Model):
    product_name = models.CharField(max_length=100, help_text="project name")


    def __str__(self):
        return self.product_name