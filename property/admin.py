from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('address', 'town_district', 'town')
    readonly_fields = ['created_at']


admin.site.register(Flat, FlatAdmin)
