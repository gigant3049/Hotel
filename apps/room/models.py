from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media/rooms', blank=True, null=True)


class Room(models.Model):
    title = models.CharField(max_length=225)
    cost = models.IntegerField(default=0)
    size = models.IntegerField()
    capacity = models.IntegerField()
    bed = models.IntegerField()
    image = models.ImageField(upload_to='media/rooms')
    description = models.TextField()


class RoomReview(models.Model):
    name = models.CharField(max_length=225)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/rooms', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room.title} - Check-in: {self.check_in}, Check-out: {self.check_out}, Adults: {self.adults}, Children: {self.children}"

    @staticmethod
    def is_room_booked(room_id, check_date):
        # Query bookings where the given room is booked on the input date
        bookings_on_date = Booking.objects.filter(room_id=room_id, check_in__lte=check_date, check_out__gt=check_date)
        return bookings_on_date.exists()