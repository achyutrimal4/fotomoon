from django.db import models
import uuid

# Create your models here.
    
    
class ContactMail (models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=200, null=True, blank=False)
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=200, null=True, blank=False)
    message = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str ( self.subject) 
    
    class Meta:
        ordering = ['is_read', '-created']
        

class Booking (models.Model):
    SERVICES = (
        ('modelling', 'Modelling'),
        ('wedding', 'Wedding'),
        ('reception', 'Reception'),
        ('engagement', 'Engagement'),
        ('family_shoot', 'Family Shoot'),
        ('maternity', 'Maternity Shoot'),
        ('family_events', 'Family Events'),
        ('videography', 'Videography'),
        ('people_and_place', 'People and Place'),
        ('other', 'Other'),
        
    )
    service_type = models.CharField(max_length=250, choices =SERVICES, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=200, null=True, blank=False)
    phone_number = models.IntegerField()
    date = models.DateField(verbose_name="Select Date")
    message = models.TextField(null=True)
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str ( self.full_name) 
    
    class Meta:
        ordering = ['is_cancelled', 'is_confirmed', '-created',  ]