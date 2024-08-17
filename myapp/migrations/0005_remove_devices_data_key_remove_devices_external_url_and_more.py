# Generated by Django 5.0.8 on 2024-08-15 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_devices_external_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='data_key',
        ),
        migrations.RemoveField(
            model_name='devices',
            name='external_url',
        ),
        migrations.RemoveField(
            model_name='devices',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='devices',
            name='routing_url',
        ),
        migrations.AddField(
            model_name='devices',
            name='Device_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='devices',
            name='points',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
            preserve_default=False,
        ),
    ]
