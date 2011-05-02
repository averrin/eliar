from django.contrib import admin
from accounts.models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(UserProfile, ProfileAdmin)
