# Generated by Django 3.1.3 on 2020-11-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_deliveryaddress_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryaddress',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
    ]
