from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def home(request):
  blogs = Blog.objects.all()
  return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
  detailed_blog = get_object_or_404(Blog, pk=id)
  return render(request, 'detail.html', {'blog': detailed_blog})

def new(request):
  return render(request, 'new.html')

def create(request):
  new_blog = Blog()
  new_blog.title = request.POST['title']
  new_blog.writer = request.POST['writer']
  new_blog.body = request.POST['body']
  new_blog.save()

  return redirect('detail', new_blog.id)

def edit(request, id):
  blog_to_edit = get_object_or_404(Blog, pk=id)

  return render(request, 'edit.html', {'blog' : blog_to_edit})

def update(request, id):
  blog_to_update = get_object_or_404(Blog, pk=id)
  blog_to_update.title = request.POST['title']
  blog_to_update.writer = request.POST['writer']
  blog_to_update.body = request.POST['body']
  blog_to_update.save()

  return redirect('detail', blog_to_update.id)

def delete(request, id):
  blog_to_delete = get_object_or_404(Blog, pk=id)
  blog_to_delete.delete()

  return redirect('home')