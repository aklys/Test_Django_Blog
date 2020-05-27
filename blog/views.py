from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Blog
from .forms import BlogForm


def blog_list(request):
    return render(request, 'blog/index.html', {'blogs': Blog.objects.all})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

def blog_new(request):
    try:        
        new = Blog()
        new.title = request.POST['title']
        new.post = request.POST['post']
        new.slug = request.POST['slug']
        new.save()
        return HttpResponseRedirect(reverse('blog:blog_list'))
        print("new item")
    except:
        return render(request, 'blog/new.html')

def blog_edit(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.title = request.POST['title']
        blog.post = request.POST['post']
        blog.slug = request.POST['slug']
        blog.save()
        return render(request, 'blog/index.html', {'blogs': Blog.objects.all})
    except:
        return HttpResponseRedirect(reverse('blog:blog_list'))

def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return HttpResponseRedirect(reverse('blog:blog_list'))
