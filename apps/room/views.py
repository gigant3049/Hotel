from django.shortcuts import render
from django.views.generic import TemplateView


class RoomView(TemplateView):
    template_name = 'room/room.html'


class SingleRoomView(TemplateView):
    template_name = 'room/single-room.html'
