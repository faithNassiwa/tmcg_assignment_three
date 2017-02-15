from django.contrib import admin
from django.contrib.admin import sites
from django.contrib.admin.sites import AdminSite
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'uuid', 'name', 'count', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['id', 'name']


# Register your models here.
admin.site.register(Group, GroupAdmin)
