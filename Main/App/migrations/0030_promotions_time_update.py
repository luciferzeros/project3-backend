# Generated by Django 3.1.3 on 2021-01-25 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_auto_20210116_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotions',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
