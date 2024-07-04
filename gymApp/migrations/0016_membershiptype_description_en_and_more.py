# Generated by Django 5.0.4 on 2024-05-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0015_membershiptype_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiptype',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='membershiptype',
            name='description_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='membershiptype',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='membershiptype',
            name='name_ja',
            field=models.CharField(max_length=200, null=True),
        ),
    ]