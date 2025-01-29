from django.urls import path
from django_qr_app.views import generate_qr_code

urlpatterns = [
    path('', generate_qr_code, name='generate_qrcode')
]