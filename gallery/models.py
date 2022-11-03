from pickle import FALSE
from django.db import models
from django.conf import settings
import uuid

# Create your models here.


class Photo (models.Model):
    description = models.CharField(null=True, blank=False, max_length=250)
    photo = models.ImageField(upload_to='images/gallery/', blank=False)
    uploaded = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)  
    
    def __str__(self):
        return self.description
    
class PhotoPortfolio(models.Model):
    description = models.CharField(null=True, blank=False, max_length=250)
    photo = models.ImageField(upload_to='images/portfolio/', blank=False)
    portfolio = models.ForeignKey(
        'Portfolio', verbose_name="Portfolio", on_delete=models.CASCADE, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)  
    
    def __str__(self):
        return self.description    
    
class Portfolio(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Portfolio Name")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    photo = models.ImageField(upload_to='images/portfolio/', blank=False,null=True, verbose_name="Cover Photo")
    created= models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
