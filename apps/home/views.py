from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import UltimateSolutions, Testimonials, Entertainment, Feedback, Services
from apps.room.models import Room
from apps.blog.models import Article
from apps.room.forms import BookingForm


class HomeView(ListView):
    model = Testimonials
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = BookingForm()
        context['Services'] = Services.objects.all()[:5]
        context['Room_lst_two'] = Room.objects.all()[:2]
        context['Feedback'] = Feedback.objects.all()[:4]
        context['latestNews'] = Article.objects.all()[:3]
        context['date_format'] = "M d, Y"
        context['Entertainment'] = Entertainment.objects.all()[:5]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         # room_id = form.cleaned_data['room']
    #         # room = get_object_or_404(Room, id=room_id)
    #         booking = form.save(commit=False)
    #         # booking.room = room
    #         booking.user = request.user
    #         booking.save()
    #         return redirect('.')
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))


class AboutView(ListView):
    model = UltimateSolutions
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['ultimate'] = UltimateSolutions.objects.all()[:3]
        context['testimonials'] = Testimonials.objects.latest('id')
        return context
