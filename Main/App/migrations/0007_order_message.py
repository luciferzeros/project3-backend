# Generated by Django 3.1.3 on 2020-11-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20201126_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
