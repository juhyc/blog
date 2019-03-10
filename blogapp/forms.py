from django import forms
from .models import Blog

class BlogPost(forms.Form): 
    email = forms.EmailField()