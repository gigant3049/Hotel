from urllib import request
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import CommentForm
from .models import Article, Tag, Instagram, Comment


class BlogView(ListView):
    model = Article
    template_name = 'blog/blog.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = context['articles']

        for article in articles:
            article.sub_articles = article.sub_article.all()

        context['recentArticles'] = Article.objects.order_by('-id')[:4]
        context['tags'] = Tag.objects.all()
        context['date_format'] = "M d, Y"
        context['instagrams'] = Instagram.objects.order_by('-id')[:6]
        return context


class BlogDetailView(DetailView, CreateView):
    model = Article
    template_name = 'blog/single-blog.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    form_class = CommentForm
    success_url = reverse_lazy('blog:single-blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, slug=self.kwargs['slug'])
        sub_articles = article.sub_article.all()
        article_tags = article.tags.all()
        tags = Tag.objects.all()
        comments = Comment.objects.all()
        context['comments'] = comments
        context['article'] = article
        context['sub_articles'] = sub_articles
        context['article_tags'] = article_tags
        context['tags'] = tags
        context['date_format'] = "M d, Y"
        context['instagrams'] = Instagram.objects.order_by('-id')[:6]
        context['recentArticles'] = Article.objects.order_by('-id')[:4]
        context['form'] = CommentForm
        return context

    def form_valid(self, form):
        article = get_object_or_404(Article, slug=self.kwargs['slug'])
        form.instance.article = article
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:single-blog', kwargs={'slug': self.kwargs.get('slug')})
