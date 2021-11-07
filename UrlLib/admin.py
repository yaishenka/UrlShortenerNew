from django.contrib import admin
from . import models


class UrlAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Url, UrlAdmin)
