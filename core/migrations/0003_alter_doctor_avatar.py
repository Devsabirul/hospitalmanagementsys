# Generated by Django 4.2.2 on 2023-06-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_doctor_contact_num_remove_doctor_departments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="avatar",
            field=models.ImageField(
                default="media/default/user.jpg", upload_to="Doctor Image"
            ),
        ),
    ]
