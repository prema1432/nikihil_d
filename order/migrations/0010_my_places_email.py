# Generated by Django 5.0.6 on 2024-06-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0009_my_places_website"),
    ]

    operations = [
        migrations.AddField(
            model_name="my_places",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
