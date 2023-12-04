from django.db import models

# Create your models here.
class Kegiatan(models.Model):
    namaKegiatan = models.CharField(max_length=200)
    deskripsiKegiatan = models.TextField()
    waktuKegiatan = models.DateTimeField("Waktu Kegiatan")