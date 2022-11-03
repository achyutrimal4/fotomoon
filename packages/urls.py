from django.urls import path
from . import views
urlpatterns = [
    path('packages/', views.packages, name='packages'),
    path('manage-packages', views.manage_packages, name='manage_packages'),
]