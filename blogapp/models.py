from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.title)

    # def get_absolute_url(self):
    #     return f'/blog/{self.pk}/' 

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)