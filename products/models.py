from pyexpat import model
from django.db import models
from more_itertools import quantify

class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantify = models.IntegerField()
    
    def __str__(self):
        return self.description