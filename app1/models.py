from django.contrib.auth.models import User
from django.db import models
import datetime
from vendorapp.models import Product


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    pro=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    total=models.IntegerField()

    def __str__(self):
        return self.pro.name

class Order(models.Model):

    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    country=models.CharField(max_length=200)
    address = models.CharField(max_length=50, default='', blank=True)
    paymentmode=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default='', blank=True)
    zip=models.CharField(max_length=6)
    date = models.DateField(default=datetime.datetime.today)
    info=models.CharField(max_length=100,default='',blank=True,null=True)
    orderstatus = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=100, choices=orderstatus, default='Pending')



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img")
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    total_price = models.IntegerField()



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist for {self.user.username}"