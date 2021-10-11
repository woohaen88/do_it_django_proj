from typing import List
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class PostListView(ListView):
    model = Post
    ordering = '-pk'
    # context_object_name = 'post_lists'
    template_name = 'blogapp/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'target_user'
    template_name = 'blogapp/detail.html'

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blogapp/list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blogapp/list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )