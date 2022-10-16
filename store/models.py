import datetime
from django.db import models
import os 
from django.contrib.auth.models import User


# Create your models here.

def get_file_path(request , filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField( max_length=150, null=False, blank=False)
    name = models.CharField( max_length=150, null=False, blank=False)
    image = models.ImageField( upload_to=get_file_path, null=True , blank=True)
    description = models.TextField(max_length=500 , null=False , blank=False)
    status = models.BooleanField(default=False, help_text="0-default , 1-hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False , blank=False)
    meta_keywords = models.CharField(max_length=150, null=False , blank=False)
    meta_description = models.CharField(max_length=1000, null=False , blank=False)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name


class Product (models.Model):
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    slug = models.CharField( max_length=150 , blank=False , null=False)
    name = models.CharField( max_length=150 , blank=False , null=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=300 , null=False , blank=False )
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500 , null=False , blank=False )
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField( max_length=150 , blank=False , null=False)
    
    meta_title = models.CharField(max_length=150, null=False , blank=False)
    meta_keywords = models.CharField(max_length=150, null=False , blank=False)
    meta_description = models.CharField(max_length=1000, null=False , blank=False)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField( max_length=150 , blank=False , null=False)
    created_at = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return self.name

class Outlets(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField( max_length=150 , blank=False , null=False)
    image = models.ImageField( upload_to=get_file_path, null=True , blank=True)
    description = models.TextField(max_length=500 , null=False , blank=True )
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name


class Servicemen(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE , default = 1)
    outlet = models.ForeignKey(Outlets, on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField( max_length=150 , blank=False , null=False)
    threshold = models.CharField( max_length=150 , blank=True , null=False)
    service = models.CharField( max_length=150 , blank=True , null=False)
    specialities = models.CharField( max_length=150 , blank=True , null=False)
    price = models.IntegerField()
    image = models.ImageField( upload_to=get_file_path, null=True , blank=True)
    created_at = models.DateTimeField( auto_now_add=True)
    

    def __str__(self):
        return self.name

class Menuitem(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE , default = 1 )
    outlet = models.ForeignKey(Outlets, on_delete=models.CASCADE , null=True , blank=True)
    servicemen= models.ForeignKey(Servicemen, on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField( max_length=150 , blank=False , null=False)
    image = models.ImageField( upload_to=get_file_path, null=True , blank=True)
    description = models.TextField(max_length=500 , null=False , blank=True )
    price = models.CharField( max_length=150 , blank=False , null=False)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlets, on_delete=models.CASCADE ,  null=True , blank=True)
    servicemen = models.ForeignKey(Servicemen, on_delete=models.CASCADE ,  null=True , blank=True)
    menuitem = models.ForeignKey(Menuitem, on_delete=models.CASCADE ,  null=True , blank=True)
    created_at = models.DateTimeField( auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150  , null=False , blank = True)
    lname = models.CharField(max_length=150  , null=False , blank = True)
    email = models.CharField(max_length=150  , null=False , blank = True)
    phone = models.CharField(max_length=150  , null=False , blank = True)
    address = models.TextField(null=False , blank = True)
    city = models.CharField(max_length=150  , null=False , blank = True)
    
    country = models.CharField(max_length=150  , null=False , blank = True)
    
    total_price = models.FloatField(null=False , blank = True)
    payment_mode = models.CharField(max_length=150, null=False , blank = True)
    payment_id = models.CharField( max_length=250, null=True , blank = True)
    orderstatuses =(
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150,choices =orderstatuses,  default='Pending')
    message = models.TextField(null=True , blank = True)
    tracking_no = models.CharField(max_length=150  , null=False , blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlets, on_delete=models.CASCADE ,  null=True , blank=True)
    servicemen = models.ForeignKey(Servicemen, on_delete=models.CASCADE ,  null=True , blank=True)
    menuitem = models.ForeignKey(Menuitem, on_delete=models.CASCADE ,  null=True , blank=True)
    created_at = models.DateTimeField( auto_now_add=True)