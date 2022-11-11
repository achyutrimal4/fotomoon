from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.login_view, name='login'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.bookings, name='bookings'),
]