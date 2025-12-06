from django.db import models
from django.utils import timezone

class Categorys(models.Model):
    category_image = models.ImageField(default='img',upload_to='dynamicimg')
    category_name = models.CharField(max_length=200)
    created = models.DateField(default=timezone.now)

class Singal_Frame_Products(models.Model):
    product_image = models.ImageField(default='img',upload_to='dynamicimg')
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_cutPrice = models.FloatField()
    product_finalprice = models.FloatField()
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    uploded_date = models.DateField(default=timezone.now)

class Group_Frame_Products(models.Model):
    product_image = models.ImageField(default='img',upload_to='dynamicimg')
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_cutPrice = models.FloatField()
    product_finalprice = models.FloatField()
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    uploded_date = models.DateField(default=timezone.now)

class Customer(models.Model):
    customer_name = models.CharField(max_length=155)
    customer_email = models.EmailField()
    customer_password = models.IntegerField()
    customer_created = models.DateField(default=timezone.now)

class Orders(models.Model):
    customer_email = models.EmailField()
    phone  =  models.IntegerField()
    image = models.ImageField(upload_to='dynamicimg',default='img')
    addres = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    totalprice = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    orderplacedate = models.DateField(default=timezone.now)

class Contact(models.Model):
    email = models.EmailField()
    msg= models.TextField(max_length=200)