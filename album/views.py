from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from album.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required(login_url='/auth/login/')
def mygallery(request):

    try:
        fcategory=request.GET['album']
        gallery = Gallery.objects.filter(album__cat=fcategory)
    except:
        gallery=Gallery.objects.all()
    
    album=Album.objects.all()
    res=render(request,'my_gallery.html',{'gallery':gallery,'album':album})
    return res

def makegallery(request):
    cat=Album.objects.all()
    res=render(request,'make_gallery.html',{'cat':cat})
    return res
    
def saveGallery(request):
    url = ''
    gallery = Gallery()
    album = Album()

    gallery.title = request.POST['title']

    if request.POST['album'] != 'default':
        # Existing album selected
        album_instance = Album.objects.get(cat=request.POST['album'])
    else:
        # New album entered
        album_cat = request.POST['newalbum']
        album_instance, created = Album.objects.get_or_create(cat=album_cat)

    gallery.album = album_instance
    gallery.image = request.FILES['myimage']
    gallery.user = request.POST['userid']

    # Save Album and Gallery instances
    album_instance.save()
    gallery.save()

    return redirect('album:mygallery')

def viewPhoto(request):
    photo=Gallery.objects.get(id=request.GET['id'])
    res=render(request,'photo.html',{'photo':photo})
    return res
def deleteImage(request):
    g=Gallery.objects.get(id=request.GET['id'])
    g.delete()    
    return redirect('album:mygallery')
