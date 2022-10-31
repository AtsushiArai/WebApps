from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='blog'),
    path('post_list', views.PostListView.as_view(), name='blog_list'),
]