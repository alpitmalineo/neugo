# Generated by Django 4.2.5 on 2023-09-05 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_seatsavailability_prefer_seat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seatsavailability',
            old_name='prefer_row',
            new_name='seat',
        ),
    ]
