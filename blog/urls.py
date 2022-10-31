from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='blog'),
    path('blog_list/', views.PostListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]