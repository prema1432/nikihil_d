# Generated by Django 5.0.6 on 2024-06-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_my_places_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="my_places",
            name="gender",
            field=models.BooleanField(default=False),
        ),
    ]
