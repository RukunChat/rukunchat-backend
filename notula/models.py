from django.db import models
from datetime import timedelta
from django.utils import timezone
from authentication.models import Pengguna

# Create your models here.

class Notula(models.Model):

    notulis = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    topik = models.CharField(max_length=255)
    poinpembahasan = models.TextField()
    hasilrapat = models.TextField()
    tanggalrapat = models.DateTimeField(auto_now_add=True)
    lokasirapat = models.TextField()

    def __str__(self):
        return self.title