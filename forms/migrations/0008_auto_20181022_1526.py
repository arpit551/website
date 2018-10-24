# Generated by Django 2.1.1 on 2018-10-22 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
