# Generated by Django 4.2.5 on 2023-09-07 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_preferseatrow_total_pax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferseatrow',
            name='seat',
        ),
        migrations.AddField(
            model_name='preferseatrow',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.busavailability'),
        ),
    ]
