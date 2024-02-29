from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=120)
    email = models.EmailField()
    open_from = models.TimeField()
    open_to = models.TimeField()


class ContactUs(models.Model):
    name = models.CharField(max_length=224)
    email = models.EmailField()
    message = models.TextField()


class Partners(models.Model):
    image = models.ImageField(upload_to='media/home')
