# Generated by Django 5.0.1 on 2024-02-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='mobileno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='noofattendees',
            field=models.IntegerField(),
        ),
    ]