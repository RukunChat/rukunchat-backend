from csv import list_dialects
from django.contrib import admin
from album.models import Gallery,Album

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','image','title','album','date']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=['id','cat']
