# Generated by Django 4.2.2 on 2023-06-19 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restapi", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="updated_at",
        ),
    ]
