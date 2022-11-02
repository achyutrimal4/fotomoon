from django.urls import path
from . import views

urlpatterns=[
    path('add_blogs/', views.addBlogs, name='add_blogs'),
    path('', views.viewBlogs, name='view_blogs'),
]