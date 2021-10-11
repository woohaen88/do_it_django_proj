from typing import List
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    ordering = '-pk'
    # context_object_name = 'post_lists'
    template_name = 'blogapp/list.html'

class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'target_user'
    template_name = 'blogapp/detail.html'