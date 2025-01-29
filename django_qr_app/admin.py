from django.contrib import admin
from django_qr_app.models import QRCodeLog

class QRCodeLogAdmin(admin.ModelAdmin):
    list_display = (
        "restaurant_name",
        "restaurant_link",
        "file_name",
        "qr_code_file_link",
        "is_successful",
        "created_at",
    )
    list_filter = ("is_successful", "created_at")
    search_fields = ("restaurant_name", "url")

admin.site.register(QRCodeLog, QRCodeLogAdmin)
