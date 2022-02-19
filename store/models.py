import os
import uuid
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

def get_unique_filepath(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join(instance.directory_string_var,filename)

class Store(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, help_text='Name of your store')
    contact_no = PhoneNumberField(unique=True)
    created = models.DateField(auto_now_add=True, editable=False, help_text='Store started on')
    lastUpdated = models.DateField(auto_now=True, editable=False, help_text='Store last updated')
    shop_img = models.ImageField(upload_to=get_unique_filepath, blank=True)
    directory_string_var = 'shopImages/'
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    store = models.ForeignKey(Store,related_name='products', on_delete=models.CASCADE)
    title = models.CharField( max_length=80, help_text='A short title')
    description = models.CharField(max_length=700, blank=True, help_text='Detail about your product')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text='Selling price including shipping')
    created = models.DateField(auto_now_add=True, editable=False, help_text='Product added on')
    lastUpdated = models.DateField(auto_now=True, editable=False )
    product_img = models.ImageField(upload_to=get_unique_filepath, blank=True)
    publish = models.BooleanField(default=False, help_text='Publish')
    directory_string_var = 'productImages/'

    def __str__(self) -> str:
        return self.title