# Generated by Django 4.1.3 on 2023-03-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='Mobile_No',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='Pin_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='Whatsapp_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
