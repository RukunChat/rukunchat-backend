from django.db import models
from datetime import timedelta
from django.utils import timezone
from administration.models import Anggota
from authentication.models import Pengguna

# Create your models here.

class Pengumuman(models.Model):
    TOPIC_CHOICES = [
        ('Kegiatan', 'Kegiatan'),
        ('Silahturahmi', 'Silahturahmi'),
        ('Kebaikan', 'Kebaikan'),
        ('Lainnya', 'Lainnya'),
    ]

    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title