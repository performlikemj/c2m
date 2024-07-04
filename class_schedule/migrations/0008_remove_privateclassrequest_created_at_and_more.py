# Generated by Django 5.0.4 on 2024-06-13 03:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_schedule', '0007_privateclassrequest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privateclassrequest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='privateclassrequest',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='privateclassrequest',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='privateclassrequest',
            name='start_time',
        ),
        migrations.AddField(
            model_name='privateclassrequest',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='privateclassrequest',
            name='requested_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='privateclassrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='privateclassrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_class_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]