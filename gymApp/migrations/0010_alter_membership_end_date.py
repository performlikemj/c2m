# Generated by Django 5.0.4 on 2024-05-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0009_gymvisit_session_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
