# Generated by Django 5.1 on 2024-08-28 00:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('name', models.CharField(blank=True, choices=[('Slider', 'Slider'), ('Toggle Button', 'Toggle Button'), ('Push Button', 'Push Button'), ('Series', 'Series')], max_length=50, null=True)),
                ('device_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('points', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DevicesPermissionsGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permissions', models.CharField(choices=[('R', 'Read'), ('RC', 'Read and change')], max_length=2)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='node_red.devices')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('group', 'device'), name='unique_group_device')],
            },
        ),
        migrations.CreateModel(
            name='DevicesPermissionsUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permissions', models.CharField(choices=[('R', 'Read'), ('RC', 'Read and change')], max_length=2)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='node_red.devices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('user', 'device'), name='unique_user_device')],
            },
        ),
    ]
