# Generated by Django 4.2.5 on 2023-09-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_busavailability_departure_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='cities',
            new_name='city',
        ),
    ]
