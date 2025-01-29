from django.shortcuts import render
from django_qr_app.forms import QRCodeForm
from django_qr_app.models import QRCodeLog
import qrcode
import os
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.utils.timezone import now

def index(request):
    return render(request, "index.html")

def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        
        if form.is_valid():
            res_name = form.cleaned_data["restaurant_name"]
            url = form.cleaned_data["url"]
            file_name = res_name.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            
            qr_log = QRCodeLog(
                restaurant_name=res_name,
                url=url,
                file_name=file_name,
                created_at=now()
            )

            try:
                # Generate QR Code
                qr = qrcode.make(url)
                qr.save(file_path)  # Save the QR code to the media directory
                
                qr_url = os.path.join(settings.MEDIA_URL, file_name)
                
                # Update log for successful generation
                qr_log.qr_code_path = qr_url
                qr_log.is_successful = True
                qr_log.save()

                context = {
                    "res_name": res_name,
                    "qr_url": qr_url,
                    "file_name": file_name,
                }
                return render(request, "qr_result.html", context)

            except PermissionDenied:
                # Handle permission errors
                error_message = "Permission denied while saving the QR code. Please check your file permissions."
                messages.error(request, error_message)
                
                qr_log.error_message = error_message
                qr_log.is_successful = False
                qr_log.save()

                return render(request, "generate_qr_code.html", {"form": form})

            except Exception as e:
                # Handle other exceptions
                error_message = f"An unexpected error occurred: {str(e)}"
                messages.error(request, error_message)
                
                qr_log.error_message = error_message
                qr_log.is_successful = False
                qr_log.save()

                return render(request, "generate_qr_code.html", {"form": form})
        
        else:
            # Log form validation failure
            error_message = "Invalid form submission. Please enter valid data."
            messages.error(request, error_message)
            QRCodeLog.objects.create(
                restaurant_name=request.POST.get("restaurant_name", ""),
                url=request.POST.get("url", ""),
                error_message=error_message,
                is_successful=False,
                created_at=now()
            )
            return render(request, "generate_qr_code.html", {"form": form})
    
    else:
        form = QRCodeForm()
        return render(request, "generate_qr_code.html", {"form": form})
