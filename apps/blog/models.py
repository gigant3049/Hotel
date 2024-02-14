from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=225)


class Article(models.Model):
    title = models.CharField(max_length=225)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/blog')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    content = models.TextField()
    is_quote = models.BooleanField(default=False)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='sub_article')


class Instagram(models.Model):
    image = models.ImageField(upload_to='media/blog')


class Comment(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/blog')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)