from csv import list_dialects
from django.contrib import admin
from album.models import User,Gallery,Album,RW,RT

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','user','image','title','album','date']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','realname','emailid','password','rt']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=['id','cat','user']

@admin.register(RW)
class RWAdmin(admin.ModelAdmin):
    list_display = ['nomor', 'kecamatan', 'kabupaten', 'provinsi']

@admin.register(RT)
class RTAdmin(admin.ModelAdmin):
    list_display = ['rw', 'nomor']