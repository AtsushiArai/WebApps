from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Blog
from .forms import PostCreateForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'blog/blog.html'

class PostListView(generic.ListView):
    model = Blog

class PostCreateView(generic.CreateView):
    model = Blog
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:blog_list')

def blog(request):
    return render(request, 'blog/blog.html')