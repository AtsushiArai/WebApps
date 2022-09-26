from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'blog/blog.html'

class PostListView(generic.ListView):
    model = Blog


def blog(request):
    pass