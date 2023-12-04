# Generated by Django 4.2.7 on 2023-12-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0014_alter_user_rt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='user',
        ),
        migrations.AddField(
            model_name='album',
            name='rt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='gallery',
            name='rt',
            field=models.IntegerField(default=1),
        ),
    ]
