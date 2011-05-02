from django.contrib import admin
from main.models import inviteRequest

class inviteRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'about')

admin.site.register(inviteRequest, inviteRequestAdmin)
