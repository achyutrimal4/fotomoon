from django.db import models

# Create your models here.
class Packages(models.Model):
    AVAILABILITY = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='images/packages/', blank=False, verbose_name="Cover Photo")
    available = models.CharField(max_length=200, choices = AVAILABILITY, verbose_name="Is available?")
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return str ( self.title) 
    
    class Meta:
        ordering = ['available', '-created']
