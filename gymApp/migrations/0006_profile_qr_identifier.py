# Generated by Django 5.0.4 on 2024-05-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0005_remove_membershiptype_price_yen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qr_identifier',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]