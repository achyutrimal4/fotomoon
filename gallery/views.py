from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import PhotoForm, PortfolioForm, PhotoPortfolioForm
from .models import Photo, Portfolio, PhotoPortfolio
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={}
    return render (request, 'gallery/home.html', context)

@login_required(login_url='login')
def add_photo(request):
    context={}
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo was successfully uploaded.')
            return redirect('gallery')
        else:
            form = PhotoForm(request.POST, request.FILES)
    context = {'form': form}
    return render (request, 'gallery/add_photo.html', context)

def gallery(request):
    gallery = Photo.objects.all().order_by('-uploaded')
    context = {'gallery': gallery}
    return  render (request, 'gallery/gallery.html', context)

def portfolio(request):
    portfolio = Portfolio.objects.all().order_by('-created')
    context = {'portfolio': portfolio}
    return render (request, 'gallery/portfolios.html', context)

def singlePortfolio(request):
    context={}
    return render (request, 'gallery/singlePortfolio.html', context)

@login_required(login_url='login')
def managePortfolio(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New portfolio created.')
            return redirect('portfolio')
        else:
            form = PortfolioForm(request.POST, request.FILES)
    context={'form':form}
    return render (request, 'gallery/managePortfolio.html', context)