import time

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/blog')
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(str(self.title))
            timestamp = str(int(time.time()))
            self.slug = f"{slug}-{timestamp}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    content = models.TextField()
    is_quote = models.BooleanField(default=False)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='sub_article')


class Instagram(models.Model):
    image = models.ImageField(upload_to='media/blog')


class Comment(models.Model):
    parent = models.ForeignKey('self', models.SET_NULL, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/blog')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def children(self):
        if not self.parent:
            return Comment.objects.filter(top_level_comment_id=self.id)
        return None


@receiver(pre_save, sender=Comment)
def pre_save_comments(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id
