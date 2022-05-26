from django.db import models

class seller(models.Model):
    name=models.CharField(max_length = 100)
    age=models.IntegerField(help_text ='age seller')
    phtone=models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.name, self.age)

class products(models.Model):
    namep=models.CharField(max_length = 100)
    description=models.TextField(help_text='this is description')
    seller=models.ForeignKey(seller,on_delete =models.CASCADE)
    price=models.IntegerField()
    product_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return '{} {} '.format(self.namep, self.description)

