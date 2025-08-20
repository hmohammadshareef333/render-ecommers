from django.contrib import admin
from .models import Products,CartModel

# Register your models here.


class products_admin(admin.ModelAdmin):
    list_display=['id','category','name','desc','price','sale','trending','image']


admin.site.register(Products,products_admin)
admin.site.register(CartModel)