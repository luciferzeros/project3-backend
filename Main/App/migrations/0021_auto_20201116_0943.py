# Generated by Django 3.1.3 on 2020-11-16 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0020_deliveryaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaddress',
            name='on_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to=settings.AUTH_USER_MODEL),
        ),
    ]
