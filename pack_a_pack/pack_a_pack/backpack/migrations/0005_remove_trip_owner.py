# Generated by Django 2.0.5 on 2018-06-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backpack', '0004_trip_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='owner',
        ),
    ]
