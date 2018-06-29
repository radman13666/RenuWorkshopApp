from django.contrib import admin
from .models import Workshop,Person,Track,Sponsor,Instructor,Attendee


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




# Register your models here.
admin.site.register(Workshop,WorkAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Sponsor,SponsorAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Attendee, AttendeeAdmin)

