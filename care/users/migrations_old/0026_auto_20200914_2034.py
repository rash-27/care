# Generated by Django 2.2.11 on 2020-09-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0025_auto_20200914_2027"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.IntegerField(
                choices=[
                    (3, "Pharmacist"),
                    (5, "Volunteer"),
                    (10, "Staff"),
                    (15, "Doctor"),
                    (25, "DistrictLabAdmin"),
                    (29, "DistrictReadOnlyAdmin"),
                    (30, "DistrictAdmin"),
                    (35, "StateLabAdmin"),
                    (39, "StateReadOnlyAdmin"),
                    (40, "StateAdmin"),
                ]
            ),
        ),
    ]