# Generated by Django 4.2.2 on 2023-06-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restapi", "0003_rename_name_complaint_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaint",
            name="latitude",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="longitude",
            field=models.FloatField(null=True),
        ),
    ]
