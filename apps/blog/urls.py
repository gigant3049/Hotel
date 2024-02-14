from django.urls import path
from .views import BlogView, BlogSingle

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('single_blog/', BlogSingle.as_view(), name='single-blog')
]