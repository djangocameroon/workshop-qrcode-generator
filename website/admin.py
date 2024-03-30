from django.contrib import admin

from website.models import DataInformation


@admin.register(DataInformation)
class DataInformationAdmin(admin.ModelAdmin):
    list_display = ("uuid", "qr_code", "created_at")
    ordering = ("-created_at",)
