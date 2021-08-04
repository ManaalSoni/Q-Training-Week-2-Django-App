from django.db import models
from django.contrib.auth.models import User
from .helper import *

# Create your models here. 
# the classes and their attributes define the database. 

class Author(models.Model):
    name = models.CharField(max_length=1000)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class BlogPosts(models.Model): # class name same as BlogModel from video
    blog_name = models.CharField(max_length=1000)
    blog_author = models.CharField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.blog_name

    def save(self, *args, **kwargs):
        from blog.helper import generate_slug
        self.slug=generate_slug(self.blog_name)
        super(BlogPosts, self).save(*args, **kwargs)

