from django.contrib import admin
from .models import BlogPosts, Profile, Author

admin.site.register(Author)
admin.site.register(BlogPosts)
admin.site.register(Profile)