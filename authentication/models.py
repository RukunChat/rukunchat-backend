from django.db import models
from django.contrib.auth.models import User


class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    nik = models.BigIntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='media/users', null=True, blank=True)  # Allow null values
    active = models.BooleanField()