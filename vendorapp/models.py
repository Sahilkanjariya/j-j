from django.db import models

from adminapp.models import Category,Subcategory

from adminapp.models import Vendor

ava=(
    ('in stock','In stock'),
    ('out of stock ','Out of stock'),
)



t=(
    ('new','new'),
    ('trendding', 'trendding'),
    ('sale','sale'),
)
# Create your models here.
class Product(models.Model):
    vid=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,blank=True)
    cid=models.ForeignKey(Category,on_delete=models.CASCADE,default="")
    sid=models.ForeignKey(Subcategory,on_delete=models.CASCADE,default="",blank=True,null=True)
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.CharField(max_length=500)
    availability=models.CharField(max_length=200,choices=ava,default='',null=True,blank=True)
    pieces=models.IntegerField()
    sku=models.CharField(max_length=20,default='',null=True,blank=True)
    image=models.FileField()
    image1=models.FileField()
    image2=models.FileField()
    image3=models.FileField()
    Tag=models.CharField(max_length=250,choices=t,default='',null=True)
    discount_percentage = models.IntegerField( null=True, blank=True)

    def discounted_price(self):
        if self.discount_percentage is not None:
            discount = self.price * (self.discount_percentage / 100)
            discounted_price = self.price - discount
            return discounted_price
        else:
            return self.price



