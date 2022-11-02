from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import PhotoForm
from .models import Photo

# Create your views here.
def home(request):
    context={}
    return render (request, 'gallery/home.html', context)

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