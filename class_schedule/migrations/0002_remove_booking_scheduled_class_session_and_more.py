# Generated by Django 5.0.4 on 2024-04-19 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='scheduled_class',
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('recurring', models.BooleanField(default=False, help_text='Is this session recurring weekly?')),
                ('class_meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='class_schedule.class')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='class_schedule.session'),
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]