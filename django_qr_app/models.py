from django.db import models
from django.utils.timezone import now
from django.utils.html import format_html

class QRCodeLog(models.Model):
    restaurant_name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    file_name = models.CharField(max_length=100)
    qr_code_path = models.URLField(max_length=500, blank=True, null=True)
    is_successful = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    def restaurant_link(self):
        return format_html('<a href="{}" target="_blank">{}</a>', self.url, self.url)
    
    restaurant_link.short_description = "Restaurant Link"

    def qr_code_file_link(self):
        if self.qr_code_path:
            # Generate an HTML link to open the QR code file
            return format_html('<a href="{}" target="_blank">Open QR Code</a>', self.qr_code_path)
        return "No QR Code"

    qr_code_file_link.short_description = "QR Code File"

    def __str__(self):
        return f"{self.restaurant_name} - {'Success' if self.is_successful else 'Failed'}"
