from django.http import JsonResponse
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Post, Comment

class Index(ListView):
    def get(self, req):
        context = {
            'posts': Post.objects.all()
        }
        return render(req, 'posts/index.html', context)

class Create(ListView):
    def get(self, req):
        return render(req, 'posts/create.html')

class Show(ListView):
    def get(self, req, id):
        post = Post.objects.get(pk=id)
        context = {
            'post': post
        }
        return render(req, 'posts/show.html', context)

class Store(ListView):
    def post(self, req):
        post = Post.objects.create(
            title = req.POST.get('title'),
            body = req.POST.get('body'),
            published = req.POST.get('published')
        )
        messages.success(req, 'Post saved successfully.')
        return redirect('posts:show', id=post.id)

class Edit(ListView):
    def get(self, req, id):
        post = Post.objects.get(pk=id)
        context = {
            'post': post
        }
        return render(req, 'posts/edit.html', context)

class Update(ListView):
    def post(self, req, id):
        post = Post.objects.get(pk=id)
        post.title = req.POST.get('title')
        post.body = req.POST.get('body')
        post.published = req.POST.get('published')
        post.save()
        messages.success(req, 'Post updated successfully.')
        return redirect('posts:show', id=post.id)

class Destroy(ListView):
    def post(self, req, id):
        post = Post.objects.get(pk=id)
        post.delete()
        messages.success(req, 'Post deleted successfully.')
        return redirect('posts:index')

class CommentsStore(ListView):
    def post(self, req, id):
        post = Post.objects.get(pk=id)
        Comment.objects.create(
            body = req.POST.get('body'),
            post = post
        )
        messages.success(req, 'Comment created successfully.')
        return redirect('posts:show', id=post.id)
    