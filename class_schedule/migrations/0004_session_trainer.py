# Generated by Django 5.0.4 on 2024-04-25 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_schedule', '0003_alter_booking_session'),
        ('gym_info', '0002_contactinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='gym_info.trainer'),
        ),
    ]