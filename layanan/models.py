from django.db import models

from administration.models import RW


# Create your models here.
class Layanan(models.Model):
    RW = models.ForeignKey(RW, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    jumlah_pendaftar = models.IntegerField(default=0)