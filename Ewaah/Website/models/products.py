from django.db import models
from .customer import Customer


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0,null=True,blank=True)
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to = 'uploads/photos/')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name