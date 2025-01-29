from django.shortcuts import render
from django_qr_app.forms import QRCodeForm
import qrcode
import os
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def index(request):
    return render(request, "index.html")

def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        
        # Validate form data
        if form.is_valid():
            res_name = form.cleaned_data["restaurant_name"]
            url = form.cleaned_data["url"]
            file_name = res_name.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)  # Path to save QR code

            try:
                # Generate QR Code
                qr = qrcode.make(url)
                qr.save(file_path)  # Save the QR code to the media directory

                # If successful, create the file URL
                qr_url = os.path.join(settings.MEDIA_URL, file_name)

                context = {
                    "res_name": res_name,
                    "qr_url": qr_url,
                    "file_name": file_name,
                }
                return render(request, "qr_result.html", context)

            except PermissionDenied:
                # Handle permission errors when trying to save the file
                messages.error(request, "Permission denied while saving the QR code. Please check your file permissions.")
                return render(request, "generate_qr_code.html", {"form": form})

            except Exception as e:
                # Catch any other exceptions (e.g., disk full, unknown errors)
                messages.error(request, f"An unexpected error occurred: {str(e)}")
                return render(request, "generate_qr_code.html", {"form": form})

        else:
            # If the form is invalid, show errors
            messages.error(request, "There was an error with the form submission. Please enter valid url and try again.")
            return render(request, "generate_qr_code.html", {"form": form})
    
    else:
        form = QRCodeForm()
        return render(request, "generate_qr_code.html", {"form": form})

