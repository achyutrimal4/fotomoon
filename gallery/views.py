from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import PhotoForm, PortfolioForm, PhotoPortfolioForm
from .models import Photo, Portfolio, PhotoPortfolio
from django.contrib.auth.decorators import login_required
from packages.models import Packages
from blog.models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    context={}
    packages= Packages.objects.all().order_by('-created')[0:3]
    portfolio = Portfolio.objects.all().order_by('-created')[0]
    blog= Blog.objects.all().order_by('created')[0]
    context = {'packages':packages, 'blog':blog, 'portfolio':portfolio}
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

    
    # pagination
    page = request.GET.get('page')
    results = 6
    paginator=Paginator(gallery, results)    
    
    
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        gallery = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        gallery = paginator.page(page)
        
    leftIndex = (int(page) - 4)
    
    if leftIndex<1:
        leftIndex=1
        
        
    rightIndex = (int(page)+5)
    if rightIndex>paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range (leftIndex,rightIndex)

    
    context = {'gallery': gallery, 'paginator': paginator, 'custom_range': custom_range}
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

@login_required(login_url='login')
def addPortfolioPhoto(request):
    form = PhotoPortfolioForm()
    if request.method == 'POST':
        form = PhotoPortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New photo added to the portfolio.')
            return redirect('portfolio')
        else:
            form = PhotoPortfolioForm(request.POST, request.FILES)
    context = {'form': form}
    return render(request, 'gallery/add_portfolio_photo.html', context)


def about_us(request):
    return render (request, 'gallery/about.html')

def portfolio_description(request, pk):    
    portfolioObj = Portfolio.objects.get(id=pk)
    context = {'portfolio': portfolioObj}
    return render (request, 'gallery/portfolio_description.html', context)