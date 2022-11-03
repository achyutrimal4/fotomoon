from django.contrib import admin
from .models import Photo, PhotoPortfolio, Portfolio
# Register your models here.

admin.site.register(Photo)
admin.site.register(PhotoPortfolio)
admin.site.register(Portfolio)