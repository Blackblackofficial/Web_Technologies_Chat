# Generated by Django 3.1.7 on 2021-03-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='chat/static/images/'),
        ),
    ]
