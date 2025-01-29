# Generated by Django 5.1.5 on 2025-01-29 12:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QRCodeLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("restaurant_name", models.CharField(max_length=50)),
                ("url", models.URLField()),
                ("file_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "qr_code_path",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("error_message", models.TextField(blank=True, null=True)),
                ("is_successful", models.BooleanField(default=False)),
            ],
        ),
    ]
