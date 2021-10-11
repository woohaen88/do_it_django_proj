from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    head_image = models.ImageField(upload_to='blog/images/%y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%y/%m/%d/', blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.title)

    # def get_absolute_url(self):
    #     return f'/blog/{self.pk}/' 

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)