from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
]