from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = ['blog_content']
    