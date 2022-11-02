from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import PhotoForm

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
            return redirect('add_photo')
        else:
            form = PhotoForm(request.POST, request.FILES)
    context = {'form': form}
    return render (request, 'gallery/add_photo.html', context)

