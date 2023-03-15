from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Registration)
admin.site.register(FifaRegistration)
admin.site.register(CodRegistration)
admin.site.register(ValoRegistration)
admin.site.register(Contact)

@admin.register(Registration)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'number',
        'email',
        'college',
        'event_name',
        'head_name',
        'member_1'
    )
    search_fields = ['email']
    list_filter = ('event_name',)