# Generated by Django 4.2.5 on 2023-09-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_is_available_preferseatrow_is_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busavailability',
            name='departure_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='api.city'),
        ),
        migrations.AlterField(
            model_name='busavailability',
            name='destination_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='api.city'),
        ),
    ]