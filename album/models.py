# from distutils.command.upload import upload
# from pyexpat import model
# from tkinter import CASCADE
# from unicodedata import category
from django.db import models
from administration.models import Anggota
from authentication.models import Pengguna

# Create your models here.

class Album(models.Model):
    cat=models.CharField(max_length=100) 

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/')

