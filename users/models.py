from django.db import models
import uuid

# Create your models here.
    
    
# class ContactMail (models.Model):
#     sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
#     receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_mails')
#     full_name = models.CharField(max_length=255, null=True, blank=False, verbose_name='Name')
#     email = models.EmailField(max_length=200, null=True, blank=False)
#     subject = models.CharField(max_length=200, null=True, blank=False)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)
    
#     def __str__(self):
#         return str ( self.subject) 
    
#     class Meta:
#         ordering = ['is_read', '-created']