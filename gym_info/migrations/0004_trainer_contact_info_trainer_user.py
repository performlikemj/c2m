# Generated by Django 5.0.4 on 2024-06-11 19:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_info', '0003_trainer_bio_en_trainer_bio_ja_trainer_name_en_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='contact_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym_info.contactinfo'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
