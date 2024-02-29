from django.urls import path
from .views import BlogView, BlogDetailView #BlogSingle, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('single_blog/<slug:slug>', BlogDetailView.as_view(), name='single-blog'),
]