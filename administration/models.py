from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authentication.models import Pengguna


class RW(models.Model):
    nomor = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)])
    kecamatan = models.CharField(max_length=255)
    kabupaten = models.CharField(max_length=255)
    provinsi = models.CharField(max_length=255)

class RT(models.Model):
    RW = models.ForeignKey(RW, on_delete=models.CASCADE)
    nomor = models.PositiveIntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    
class Anggota(models.Model):
    RT = models.ForeignKey(RT, on_delete=models.CASCADE)
    RW = models.ForeignKey(RW, on_delete=models.CASCADE)
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)

class Pengurus(models.Model):
    '''
    semua pengurus pasti anggota
    '''
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=255)
