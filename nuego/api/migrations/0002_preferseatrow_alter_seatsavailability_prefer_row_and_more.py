# Generated by Django 4.2.5 on 2023-09-05 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferSeatRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prefer_row', models.CharField(max_length=10)),
                ('prefer_seat', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='seatsavailability',
            name='prefer_row',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prefer_row', to='api.busavailability'),
        ),
        migrations.AlterField(
            model_name='seatsavailability',
            name='prefer_seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prefer_seat', to='api.busavailability'),
        ),
    ]