import os
import subprocess
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = "Sets up the project with required installations, migrations, superuser creation, static file collection, and media directory creation"

    def handle(self, *args, **kwargs):
        try:
            # Step 1: Create the media directory if it doesn't exist
            media_dir = settings.MEDIA_ROOT
            if not os.path.exists(media_dir):
                self.stdout.write(f"Creating media directory at: {media_dir}...")
                os.makedirs(media_dir)
                self.stdout.write(self.style.SUCCESS(f"Media directory created at: {media_dir}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Media directory already exists at: {media_dir}"))

            # Step 2: Install requirements
            self.stdout.write("Installing requirements...")
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
            self.stdout.write(self.style.SUCCESS("Requirements installed successfully."))

            # Step 3: Run migrations
            self.stdout.write("Running migrations...")
            subprocess.run(["python3", "manage.py", "migrate"], check=True)
            self.stdout.write(self.style.SUCCESS("Migrations completed successfully."))

            # Step 4: Create a superuser with hardcoded credentials
            self.stdout.write("Creating superuser...")
            username = "admin"  # Hardcoded username
            email = "admin@example.com"  # Hardcoded email
            password = "password123"  # Hardcoded password

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
            else:
                self.stdout.write(self.style.WARNING("Superuser already exists. Skipping creation."))

            # Step 5: Collect static files
            self.stdout.write("Collecting static files...")
            subprocess.run(["python3", "manage.py", "collectstatic", "--noinput"], check=True)
            self.stdout.write(self.style.SUCCESS("Static files collected successfully."))

            # Step 6: Start the server (use gunicorn for production)
            self.stdout.write("Starting the server...")
            subprocess.run(["gunicorn", "django_qr_project.wsgi:application", "--bind", "0.0.0.0:8000"], check=True)

        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f"Error occurred while running: {e.cmd}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Unexpected error: {e}"))
