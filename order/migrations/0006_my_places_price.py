# Generated by Django 5.0.6 on 2024-06-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_my_places_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="my_places",
            name="price",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
