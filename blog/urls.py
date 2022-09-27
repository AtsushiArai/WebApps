from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostListView.as_view(), name="blog_list"),
    path('blog_form/', views.PostCreateView.as_view(), name="blog_form")
]