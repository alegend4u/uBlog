from django.contrib import admin
from .models import *


class MediaAdmin(admin.ModelAdmin):
    list_display = ['moment', 'type', 'file']
    exclude = ['type']


class MediaInline(admin.TabularInline):
    model = Media
    fields = ['file',]


class MomentAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]


# Register your models here.
admin.site.register(Moment, MomentAdmin)
admin.site.register(Media, MediaAdmin)
