from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite

#from .models import Workshop,Person,Instructor,Attendee

class MyAdminSite(AdminSite):
    site_header = 'RENU Workshops'
    site_title = "RENU Workshops"
    index_title = "RENU Workshops"
    site_url = "https://Workshops.renu.ac.ug"

admin_site = MyAdminSite(name='admin')
app_models = apps.get_app_config('analytics').get_models()
for model in app_models:
    admin_site.register(model)

admin_site.register(User)
