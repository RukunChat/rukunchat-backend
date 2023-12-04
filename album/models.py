# from distutils.command.upload import upload
# from pyexpat import model
# from tkinter import CASCADE
# from unicodedata import category
from django.db import models

# Create your models here.

class RW(models.Model):
    nomor=models.IntegerField()
    kecamatan=models.CharField(max_length=40)
    kabupaten=models.CharField(max_length=40)
    provinsi=models.CharField(max_length=40)

class RT(models.Model):
    # Fields for RT class
    rw = models.ForeignKey(RW, on_delete=models.CASCADE,default=None)
    nomor=models.IntegerField()

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=25)
    realname=models.CharField(max_length=40)
    emailid=models.CharField(max_length=60)
    password=models.CharField(max_length=16,)
    rt = models.ForeignKey(RT, on_delete=models.CASCADE,null=True, blank=True)
    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    user=models.CharField(max_length=40,default="admin")
    album=models.CharField(max_length=40)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/')

class Album(models.Model):
    cat=models.CharField(max_length=100) 
    user=models.CharField(max_length=40,default="admin")

