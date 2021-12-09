from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    EstReg = models.BooleanField(default=True)

class TypeProd(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    EstReg = models.BooleanField(default=True)

class ProductLine(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    EstReg = models.BooleanField(default=True)

class Product(models.Model):
    UNIT_CHOICES = [
    ('ml', 'mililitros'),
    ('L', 'Litros'),
    ('gr', 'gramos'),
    ('oz', 'onzas'),
    ]
    name = models.CharField(max_length=128)
    capacity = models.PositiveSmallIntegerField(default=0)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    description = models.TextField()
    productLine = models.ForeignKey(ProductLine, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True)
    Type = models.ForeignKey(TypeProd,on_delete=models.SET_NULL, null=True)
    #imagen
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=1)
    EstReg = models.BooleanField(default=True)


