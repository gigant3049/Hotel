from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404

from apps.home.models import Feedback
from .forms import BookingForm
from .models import Room, Services, RoomReview, Booking


class RoomView(ListView):
    model = Room
    template_name = 'room/room.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        return context

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.order_by('-id')
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        if check_in or check_out:
            rooms = rooms.filter(~Q(datas__check_in__lte=check_out) |~Q(datas__check_out__gte=check_in))
        if adults or children:
            children = int(children)
            adults = int(adults)
            rooms = rooms.filter(Q(children__gte=children) or Q(adults__gte=adults))

        paginator = Paginator(rooms, 5)
        page = request.GET.get('p')
        rooms = paginator.get_page(page)

        context = {
            'rooms': rooms,
        }
        return render(request, self.template_name, context)


class SingleRoomView(FormMixin, DetailView):
    model = Room
    template_name = 'room/single-room.html'
    context_object_name = 'room'
    form_class = BookingForm

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        room_slug = self.kwargs.get('slug')
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']
        adults = form.cleaned_data['adults']
        children = form.cleaned_data['children']
        print(room_slug)
        try:
            room = Room.objects.get(slug=room_slug)
        except Room.DoesNotExist:
            messages.error(self.request, 'The specified room does not exist.')
            return self.form_invalid(form)

        if check_in and check_out:
            Booking.objects.create(
                room=room,
                check_in=check_in,
                check_out=check_out,
                adults=adults,
                children=children
            )
            messages.success(self.request, 'The room has been successfully booked!')
            return redirect(self.get_success_url())

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms_images'] = Room.objects.order_by('-id')[:5]
        context['services'] = Services.objects.order_by('-id')[:6]
        context['reviews'] = RoomReview.objects.order_by('-id')[:3]
        context['date_format'] = "M d, Y"
        context['form'] = self.get_form()
        return context
