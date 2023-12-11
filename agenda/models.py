from django.db import models
from administration.models import Pengurus

# Create your models here.
class Kegiatan(models.Model):
    pengurus = models.ForeignKey(Pengurus, 
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    namaKegiatan = models.CharField(max_length=200)
    deskripsiKegiatan = models.TextField()
    waktuKegiatan = models.DateTimeField("Waktu Kegiatan")
    
    def __str__(self):
        return self.namaKegiatan