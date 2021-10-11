from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied



class PostUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blogapp/update.html'
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def get_success_url(self):
        return reverse('blogapp:detail', kwargs={'pk' : self.object.pk})


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'blogapp/create.html'
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
    success_url = reverse_lazy('blogapp:list')

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

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