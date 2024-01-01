from django.contrib import admin

from .models import Kat


@admin.register(Kat)
class KatAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "age")
    list_filter = ("age",)
    ordering = ("name",)
