# Generated by Django 4.2.2 on 2023-06-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_appointment_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appointment_id",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
