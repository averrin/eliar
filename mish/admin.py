from django.contrib import admin
from mish.models import Wall

class WallAdmin(admin.ModelAdmin):
    list_display = ('wall_text',)

admin.site.register(Wall, WallAdmin)
