from django.db import models


   
class Category(models.Model):
    title = models.CharField(max_length=50)
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    