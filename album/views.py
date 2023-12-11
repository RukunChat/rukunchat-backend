from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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
    url=''
    gallery=Gallery()
    album=Album()
    gallery.title=request.POST['title']
    if  request.POST['album'] != 'default':
        album=get_object_or_404(Album, cat=request.POST['album'])
    else:
        gallery.album=request.POST['newalbum']
        album.cat=request.POST['newalbum']
        album.user=request.POST['userid']
    gallery.image=request.FILES['myimage']
    gallery.user=request.POST['userid']

    gallery.album=album
    gallery.save()
    url='http://localhost:8000/album'
    return HttpResponseRedirect(url)
def viewPhoto(request):
    photo=Gallery.objects.get(id=request.GET['id'])
    res=render(request,'photo.html',{'photo':photo})
    return res
def deleteImage(request):
    g=Gallery.objects.get(id=request.GET['id'])
    g.delete()    
    return HttpResponseRedirect('http://localhost:8000/album')