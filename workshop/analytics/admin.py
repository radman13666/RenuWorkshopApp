from django.contrib import admin
from .models import Workshop, Track, Sponsor, Facilitator, Participant
# from django.apps import apps
# from django.contrib.auth.models import User
# from django.contrib.admin import AdminSite


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'start_date', 'end_date')
    list_filter = ('venue', 'host', 'sponsors', 'facilitators', 
                   'participants')
    search_fields = ('name', 'venue')


# TODO find out how to show workshops for facilitator|sponsor|participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email',
                    'institution', 'country',)  # 'workshop_attended')
    list_filter = ('gender', 'institution', 'country')  # 'workshop_attended',
    search_fields = ('first_name', 'last_name')
    save_as = True
    save_on_top = True
    # change_list_template = 'change_list_graph.html'
    #
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "attendee"
    #     return response


class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email',
                    'institution', 'country',)  # 'workshop_taught')
    list_filter = ('institution', 'gender', 'country')  # 'workshop_taught',
    search_fields = ('first_name', 'last_name')
    save_as = True
    save_on_top = True
    # change_list_template = 'change_list_graph.html'
    #
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "instructor"
    #     return response


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display = ('name', 'workshop_sponsored')
    # list_filter = ('name', 'workshop_sponsored')
    #
    # change_list_template = 'change_list_graph.html'
    #
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "sponsor"
    #     return response


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)


renu_header_str = "RENU Workshops"

admin.site.site_header = renu_header_str
admin.site.site_title = renu_header_str
admin.site.index_title = renu_header_str
admin.site.site_url = "https://workshops.renu.ac.ug"

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
# admin.site.register(Person, PersonAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Participant, ParticipantAdmin)
