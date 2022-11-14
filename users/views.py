from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.models import User
from .models import  ContactMail, Booking
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, BookingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from packages.models import Packages
from blog.models import Blog
from gallery.models import Photo, Portfolio


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
    unread_mails = ContactMail.objects.filter(is_read=False).count()
    new_bookings = Booking.objects.filter(is_confirmed=False, is_cancelled=False).count()
    package_count = Packages.objects.all().count()
    portfolio_count = Portfolio.objects.all().count()
    blog_count = Blog.objects.all().count()
    photos = Photo.objects.all().count()
    
    context = {'unread_mails': unread_mails, 'new_bookings':new_bookings, 
               'package_count':package_count,
               'portfolio_count':portfolio_count,
               'blog_count':blog_count,
               'photos':photos,}

    return render(request, 'users/admin_panel.html', context)

# def contact (request):
#     context={}
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Message successfully sent. We will get back to you soon.')
#             return redirect('contact')
#     context={'form': form}
#     return render (request, 'users/contact.html', context)
    
    

# send message

def contact(request):
    User = get_user_model()

    form = ContactForm()
    context = {}
    admin = User.objects.order_by('-is_superuser').first()
    # admin_id = admin.profile.id
    # admin_profile = User.objects.get(id=admin_id)
    recipient = admin
    sender = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receiver = recipient

            message.save()
            messages.success(
                request, 'Message successfully sent. We\'ll get back to you soon.')
            return redirect('contact')
        else:
            messages.error(
                request, 'Message could not be sent. Please try again')
            form = ContactForm(request.POST)
    context = {'admin': admin, 'form': form}
    return render(request, 'users/contact.html', context)


def view_inbox (request):
    inbox = ContactMail.objects.all()
    context ={'inbox':inbox}
    return render(request, 'users/view_contact_messages.html', context)

def read_inbox (request, id):
    inbox = ContactMail.objects.get(id=id)
    inbox.is_read = True
    inbox.save()
    context ={'inbox':inbox}
    return HttpResponseRedirect(reverse('view_inbox'))
    # return render(request, 'users/read_message.html', context)
    
    
def bookings(request):
    User = get_user_model()

    form = BookingForm()
    context = {}
    admin = User.objects.order_by('-is_superuser').first()
    # admin_id = admin.profile.id
    # admin_profile = User.objects.get(id=admin_id)
    recipient = admin
    sender = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.sender = sender
            booking.receiver = recipient

            booking.save()
            messages.success(
                request, 'Thank you for booking our service. We will contact you soon for confirmation.')
            return redirect('bookings')
        else:
            messages.error(
                request, 'Could not book. Please try again')
            form = BookingForm(request.POST)
    context = {'admin': admin, 'form': form}
    return render (request, 'users/booking.html', context)

def view_bookings (request):
    bookings = Booking.objects.all()
    context ={'bookings':bookings}
    return render(request, 'users/view_bookings.html', context)


def confirm_booking (request, id):
    booking = Booking.objects.get(id=id)
    booking.is_confirmed = True
    booking.save()
    # context ={'booking':booking}
    return HttpResponseRedirect(reverse('view_bookings'))

def cancel_booking (request, id):
    booking = Booking.objects.get(id=id)
    booking.is_cancelled = True
    booking.save()
    # context ={'booking':booking}
    return HttpResponseRedirect(reverse('view_bookings'))