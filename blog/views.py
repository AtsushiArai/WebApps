from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
# from .forms import PostCreateForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'blog/blog.html'

class PostListView(generic.ListView):
    template_name = 'blog/blog_list.html'
    model = Post

class PostDetailView(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    model = Post

# class PostCreateView(generic.CreateView):
#     model = Post
#     form_class = PostCreateForm
#     success_url = reverse_lazy('blog:blog_list')

# def blog(request):
#     return render(request, 'blog/blog.html')