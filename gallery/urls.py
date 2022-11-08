from django.urls import path
from .  import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('add-photo/', views.add_photo, name='add_photo'),
    path('gallery/', views.gallery, name='gallery'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-description/<str:pk>/', views.portfolio_description, name='portfolio_description'),
    path('manage-portfolio/', views.managePortfolio, name='manage_portfolio'),
    path('add-portfolio-photo', views.addPortfolioPhoto, name='add_portfolio_photo'),
    path('about-us/', views.about_us, name='about_us'),
]