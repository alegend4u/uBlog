from django.contrib import admin
from .models import *


class MediaInline(admin.TabularInline):
    model = Media


class MomentAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]


# Register your models here.
admin.site.register(Moment, MomentAdmin)
admin.site.register(Media)
