from django.db import models


# Create your models here.
class Layanan(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    jumlah_pendaftar = models.IntegerField(default=0)