from django.contrib import admin
from .models import Services, Testimonials, Entertainment, Feedback, UltimateSolutions


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', )


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'signature')


@admin.register(Entertainment)
class EntertainmentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'created')
    search_fields = ('name', )


@admin.register(UltimateSolutions)
class UltimateSolutionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', )
