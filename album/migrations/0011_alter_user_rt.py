# Generated by Django 4.2.7 on 2023-12-04 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0010_alter_user_rt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rt',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mygallery.rt'),
        ),
    ]
