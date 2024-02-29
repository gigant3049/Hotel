import time

from django.db import models
from django.utils.text import slugify


class Services(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/rooms', blank=True, null=True)


class Room(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(blank=True)
    cost = models.IntegerField(default=0)
    size = models.IntegerField()
    capacity = models.IntegerField()
    bed = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/rooms')
    description = models.TextField()
    adults = models.PositiveIntegerField(null=True, blank=True)
    children = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(str(self.title))
            timestamp = str(int(time.time()))
            self.slug = f"{slug}-{timestamp}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class RoomReview(models.Model):
    name = models.CharField(max_length=225)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    room = models.ManyToManyField(Room)
    image = models.ImageField(upload_to='media/rooms', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='datas', blank=True, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room.title} - Check-in: {self.check_in}, Check-out: {self.check_out}, Adults: {self.adults}, Children: {self.children}"

    @staticmethod
    def is_room_booked(room_id, check_date):
        bookings_on_date = Booking.objects.filter(room_id=room_id, check_in__lte=check_date, check_out__gt=check_date)
        return bookings_on_date.exists()
