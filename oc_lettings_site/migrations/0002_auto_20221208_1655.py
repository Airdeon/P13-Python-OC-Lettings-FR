# Generated by Django 3.0 on 2022-12-08 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("lettings", "0003_auto_20221208_1648"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
    ]
