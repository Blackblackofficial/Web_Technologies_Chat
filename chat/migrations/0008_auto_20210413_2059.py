# Generated by Django 3.1.7 on 2021-04-13 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_auto_20210413_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id'),
        ),
    ]
