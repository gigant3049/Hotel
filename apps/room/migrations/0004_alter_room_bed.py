# Generated by Django 5.0.2 on 2024-02-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='bed',
            field=models.CharField(max_length=225),
        ),
    ]
