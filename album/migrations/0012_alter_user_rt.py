# Generated by Django 4.2.7 on 2023-12-04 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0011_alter_user_rt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rt',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mygallery.rt'),
        ),
    ]
