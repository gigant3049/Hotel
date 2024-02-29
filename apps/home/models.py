from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/home', null=True, blank=True)
    content = models.TextField()
    signature = models.ImageField(upload_to='media/home')


class UltimateSolutions(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/home')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='media/home', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Entertainment(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='media/home')
