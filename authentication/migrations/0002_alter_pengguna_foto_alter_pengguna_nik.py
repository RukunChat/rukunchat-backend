# Generated by Django 4.2.7 on 2023-12-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengguna',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/users'),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='nik',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]