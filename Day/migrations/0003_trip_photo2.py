# Generated by Django 2.0.13 on 2019-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Day', '0002_trip_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='photo2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
