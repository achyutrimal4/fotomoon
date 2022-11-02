from django.db import models
import uuid

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)
    image = models.ImageField(null=True, blank=False, upload_to='images/blogs/')
    imageBy = models.CharField(max_length=200, default="Fotomoon Admin")
    author = models.CharField(
        max_length=200, default="Fotomoon Admin", null=True, blank=True)
    photo_caption = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
