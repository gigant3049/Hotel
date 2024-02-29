from django.contrib import admin
from .models import Instagram, Article, Tag, SubArticle, Comment


class SubArticleTabularInline(admin.TabularInline):
    extra = 1
    model = SubArticle
    list_display = ('is_quote', 'content')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleTabularInline, )
    list_display = ('id', 'title')
    readonly_fields = ('slug', )
    search_fields = ('title', )
    filter_horizontal = ('tags', )


@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'top_level_comment_id', 'created_date')
    search_fields = ('name', 'email')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
