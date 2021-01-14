from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_published', 'id']
    paginate_by = 5



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    context_object_name = 'post'
