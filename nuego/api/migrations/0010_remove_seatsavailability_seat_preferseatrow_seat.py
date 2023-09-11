# Generated by Django 4.2.5 on 2023-09-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_prefer_row_seatsavailability_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatsavailability',
            name='seat',
        ),
        migrations.AddField(
            model_name='preferseatrow',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.seatsavailability'),
        ),
    ]