from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


# Login and logout
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        messages.success(request, 'You are logged in as an Admin.')
        return redirect('admin_panel')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User doesnot exist')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('admin_panel')
            else:
                messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/admin_login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def admin_panel(request):
    context = {}
    return render(request, 'users/admin_panel.html', context)

def contact (request):
    context={}
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message successfully sent. We will get back to you soon.')
            return redirect('contact')
    context={'form': form}
    return render (request, 'users/contact.html', context)
    
