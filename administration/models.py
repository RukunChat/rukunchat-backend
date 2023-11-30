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

    class Meta:
        unique_together = ('nomor', 'kecamatan', 'kabupaten', 'provinsi')

class RT(models.Model):
    RW = models.ForeignKey(RW, on_delete=models.CASCADE)
    nomor = models.PositiveIntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    class Meta:
        unique_together = ('RW', 'nomor')
    
class Anggota(models.Model):
    pengguna = models.OneToOneField(Pengguna, on_delete=models.CASCADE)
    RT = models.ForeignKey(RT, on_delete=models.CASCADE)

class Pengurus(models.Model):
    anggota = models.OneToOneField(Anggota, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=255)
