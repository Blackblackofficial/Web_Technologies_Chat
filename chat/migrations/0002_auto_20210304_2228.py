# Generated by Django 3.1.7 on 2021-03-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]