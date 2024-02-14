from django.urls import path
from .views import RoomView, SingleRoomView

app_name = 'room'

urlpatterns = [
    path('room/', RoomView.as_view, name='room'),
    path('single-room/', SingleRoomView.as_view, name='single-room')
]