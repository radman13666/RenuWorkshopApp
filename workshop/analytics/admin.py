from django.contrib import admin
from .models import Workshop,Person,Track,Sponsor,Instructor,Attendee,Institution
# from django.apps import apps
# from django.contrib.auth.models import User
# from django.contrib.admin import AdminSite


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'start_date', 'end_date')
    list_filter = ('name', 'venue')
    search_fields = ('name', 'venue')


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'location')
    list_filter = ('institution_name', 'location')


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'institution', 
                    'country', 'workshop_attended')
    list_filter = ('workshop_attended', 'gender', 'institution')
    search_fields = ('first_name', 'last_name')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        response.context_data['page'] = "attendee"
        return response


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'institution', 
                    'country', 'workshop_affiliated', 'track_they_teach')
    list_filter = ('institution', 'gender', 'workshop_affiliated')
    search_fields = ('first_name', 'last_name')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        response.context_data['page'] = "instructor"
        return response


class SponsorAdmin(admin.ModelAdmin,):
    list_display = ('name', 'workshop_sponsored')
    list_filter = ('workshop_sponsored', 'name')

    change_list_template = 'change_list_graph.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        response.context_data['page'] = "sponsor"
        return response


class TrackAdmin(admin.ModelAdmin):
    list_display = ('track_title', 'associated_workshop')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'institution', 'email', 'gender')
    list_filter = ('institution', 'gender')


renu_header_str = "RENU Workshops"

admin.site.site_header = renu_header_str
admin.site.site_title = renu_header_str
admin.site.index_title = renu_header_str
admin.site.site_url = "https://workshops.renu.ac.ug"

admin.site.register(Workshop, WorkAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Institution, InstitutionAdmin)
