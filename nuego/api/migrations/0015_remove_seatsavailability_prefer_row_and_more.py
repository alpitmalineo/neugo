# Generated by Django 4.2.5 on 2023-09-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_preferseatrow_prefer_row_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatsavailability',
            name='prefer_row',
        ),
        migrations.RemoveField(
            model_name='seatsavailability',
            name='prefer_seat',
        ),
        migrations.RemoveField(
            model_name='seatsavailability',
            name='seat_number',
        ),
        migrations.AddField(
            model_name='preferseatrow',
            name='prefer_row',
            field=models.CharField(default=345, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preferseatrow',
            name='prefer_seat',
            field=models.CharField(default=5787, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preferseatrow',
            name='seat_number',
            field=models.CharField(default=66554, max_length=10),
            preserve_default=False,
        ),
    ]
