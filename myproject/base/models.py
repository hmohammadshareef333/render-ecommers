from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='default.png',upload_to='uploads')
    sale=models.BooleanField(default=False)
    trending=models.BooleanField(default=False)


class CartModel(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=1)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

