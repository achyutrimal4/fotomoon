from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def addBlogs(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog successfully added.')
            return redirect("view_blogs")
    context = {'form': form}
    return render(request, 'blog/add_blog.html', context)


def viewBlogs (request):
    context={}
    blogs = Blog.objects.all().order_by('-created')
    context={'blogs':blogs}
    return render (request, 'blog/blogs.html', context)

