from django.contrib import admin
from .models import Workshop,Person,Track,Sponsor,Instructor,Attendee
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','venue','start_date','end_date')
    list_filter = ('name','venue')
    search_fields = ('name','venue')



class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'gender','institution','workshop_attended')
    list_filter = ('workshop_attended','gender', 'institution')
    search_fields = ('first_name', 'last_name')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','institution','workshop_affiliated','track_they_teach')
    list_filter = ('institution','gender','workshop_affiliated')
    search_fields = ('first_name','last_name')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

class SponsorAdmin(admin.ModelAdmin,):
    list_display = ('name','workshop_sponsored')
    list_filter = ('workshop_sponsored','name')

class TrackAdmin(admin.ModelAdmin):
    list_display = ('track_title','associated_workshop')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','institution','email','gender')
    list_filter = ('institution','gender')


class MyAdminSite(AdminSite):
    site_header = 'RENU Workshops'
    site_title = "RENU Workshops"
    index_title = "RENU Workshops"
    site_url = "https://Workshops.renu.ac.ug"

admin_site = MyAdminSite(name='admin')
app_models = apps.get_app_config('myapp').get_models()

# for model in app_models:
#     admin_site.register(model)

admin_site.register(User)

# Register your models here.
admin.site.register(Workshop,WorkAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Attendee, AttendeeAdmin)

