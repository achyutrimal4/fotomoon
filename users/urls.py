from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.login_view, name='login'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.bookings, name='bookings'),
    path('view-messages/', views.view_inbox, name='view_inbox'),
    path('read-messages/<str:id>', views.read_inbox, name='read_inbox'),
    path('view-bookings/', views.view_bookings, name='view_bookings'),
    path('confirm-booking/<str:id>', views.confirm_booking, name='confirm_booking'),
    path('cancel-booking/<str:id>', views.cancel_booking, name='cancel_booking'),

]