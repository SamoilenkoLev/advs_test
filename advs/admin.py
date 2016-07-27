from django.contrib import admin
from .models import Advs


class AdvsAdmin(admin.ModelAdmin):
    list_display = 'date', 'name',
    search_fields = 'name', 'text',
    list_display_links = 'name',
    date_hierarchy = 'date'

admin.site.register(Advs, AdvsAdmin)
