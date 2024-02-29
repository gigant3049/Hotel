from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Contact, Partners


class ContactView(ListView):
    model = Contact
    template_name = 'contact/contact.html'
    context_object_name = 'contactData'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contactData'] = Contact.objects.latest('id')
        return context


def partners_data(request):
    return {'partnersData': Partners.objects.all()}
