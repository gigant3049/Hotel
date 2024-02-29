# Generated by Django 5.0.2 on 2024-02-27 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_room_check_in_room_check_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='room',
            name='check_out',
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='room.room'),
        ),
    ]