from django.contrib import admin

from .models import Workshop,Person,Instructor,Attendee

# Register your models here.
admin.site.register(Workshop)
admin.site.register(Instructor)
admin.site.register(Person)
admin.site.register(Attendee)
