# Generated by Django 5.0.4 on 2024-04-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('google_maps_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('tiktok_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]