from django.contrib import admin
from .models import Contact, ContactUs, Partners


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', 'email', 'open_from', 'open_to')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ('name', 'email')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
