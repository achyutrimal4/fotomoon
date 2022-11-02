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
    
# class Album(models.Model):
#     name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Album")
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)
    
#     def __str__(self):
#         return self.name