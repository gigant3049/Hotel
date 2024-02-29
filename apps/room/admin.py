from django.contrib import admin
from .models import Services, Room, RoomReview, Booking


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'size', 'capacity', 'bed', 'image')
    readonly_fields = ('slug', )


@admin.register(RoomReview)
class RoomReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'image', 'created_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'check_in', 'check_out', 'adults', 'children')