from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
import datetime

from .models import Posts


class UserBlogListView(ListView):
    model = Posts
    template_name = 'blog/user_blog.html'
    context_object_name = 'posts'

    ordering = ['-date']


class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/posts_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Posts
    fields = ['title', 'full_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date = datetime.datetime.now()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Posts
    success_url = '/'
    template_name = 'blog/posts_delete.html'
    context_object_name = 'post'


