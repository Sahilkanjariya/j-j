from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class emp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(null=True,blank=True)
    is_emp=models.BooleanField(default=False)
    profile=models.ImageField(default='user.jpg',upload_to='profile')

class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(null=True,blank=True)
    is_vendor=models.BooleanField(default=False)
    profile=models.ImageField(default='user.jpg',upload_to='profile')
    otp = models.IntegerField(null=True, blank=True)


class Category(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='category')

class Subcategory(models.Model):
    category=models.ForeignKey(Category,models.CASCADE)
    name=models.CharField(max_length=25)
    image\
        =models.ImageField(upload_to='Subcategory')
