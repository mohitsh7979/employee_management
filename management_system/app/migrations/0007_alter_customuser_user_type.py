# Generated by Django 4.1.3 on 2023-03-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_resourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin')], default=1, max_length=50),
        ),
    ]
