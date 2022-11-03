from django.shortcuts import render, redirect
from . forms import PackageForm
from django.contrib import messages
from .models import Packages
# Create your views here.


def packages(request):
    context={}
    packages = Packages.objects.all()
    context={'packages': packages}
    return render (request, 'packages/packages.html', context)

def manage_packages(request):
    context={}
    form = PackageForm()
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Package added.')
            return redirect('packages')
        else:
            form = PackageForm(request.POST, request.FILES)       
    
    context={'form':form}
    return render (request, 'packages/manage_packages.html', context)
