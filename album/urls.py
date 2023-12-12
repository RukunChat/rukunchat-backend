from django.urls import path
from album.views import *

app_name = 'album'

urlpatterns = [
    path('',mygallery,name='mygallery'),
    path('add-photo',makegallery,name='makegallery'),
    path('save-gallery',saveGallery,name='savegallery'),
    path('view-photo',viewPhoto,name='photo'),
    path('delete-image',deleteImage,name='deleteimage'),
    
]
