from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from album.models import *

def index(request):
    return render(request,'album/index.html')

def signup(request):
    res=render(request,'album/signup.html')
    return res

def checkName(request):
    user=User.objects.filter(username=request.GET['username'])
    if not user:
        return HttpResponse('true')
    else:
        return HttpResponse('false')

def saveUser(request):
    user=User()
    user.username=request.POST['username']
    user.realname=request.POST['realname']
    user.emailid=request.POST['emailid']
    user.password=request.POST['password']
    user.save()
    return HttpResponseRedirect('http://localhost:8000/login')

def login(request):
    d1={}
    try:
        if request.GET['username']=='invalid':
            d1['errormsg']='Username Invalid'     
    except:
        d1['errormsg']=''
    try:
        if request.GET['password']=='invalid':
            d1['errormsg']='Password Invaild'
    except:
        pass
    res=render(request,'album/login.html',d1)
    return res

def loginValidation(request):
    url=''
    try:
        user=User.objects.get(username=request.POST['username'])
        if user.username==request.POST['username'] and user.password==request.POST['password']:
            request.session['username']=user.username
            request.session['realname']=user.realname
            url='http://localhost:8000'
        else:
            url='http://localhost:8000/login?password=invalid'
    except:
        url='http://localhost:8000/login?username=invalid'
                
    return HttpResponseRedirect(url)

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/login')

def mygallery(request):
    try:
        fcategory=request.GET['album']
        gallery=Gallery.objects.filter(user=request.session['username'],album=fcategory)
    except:
        gallery=Gallery.objects.filter(user=request.session['username'])

    album=Album.objects.filter(user=request.session['username'])
    res=render(request,'album/my_gallery.html',{'gallery':gallery,'album':album})
    return res

def makegallery(request):
    cat=Album.objects.filter(user=request.session['username'])
    res=render(request,'album/make_gallery.html',{'cat':cat})
    return res
    
def saveGallery(request):
    url=''
    gallery=Gallery()
    album=Album()
    gallery.title=request.POST['title']
    if  request.POST['album'] != 'default':
        gallery.album=request.POST['album']
    else:
        gallery.album=request.POST['newalbum']
        album.cat=request.POST['newalbum']
        album.user=request.POST['userid']
    gallery.image=request.FILES['myimage']
    gallery.user=request.POST['userid']
    album.save()
    gallery.save()
    url='http://localhost:8000/my-gallery'
    return HttpResponseRedirect(url)
def viewPhoto(request):
    photo=Gallery.objects.get(id=request.GET['id'])
    res=render(request,'album/photo.html',{'photo':photo})
    return res
def deleteImage(request):
    g=Gallery.objects.get(id=request.GET['id'])
    g.delete()    
    return HttpResponseRedirect('http://localhost:8000/my-gallery')