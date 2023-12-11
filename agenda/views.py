from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from administration.models import Anggota, Pengurus
from authentication.models import Pengguna

from .models import Kegiatan
from .forms import KegiatanForm

@login_required(login_url='/auth/login/')
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'unauthenticated_access.html')
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthenticated_access.html')
    try:
        anggota = Anggota.objects.get(pengguna=pengguna)
    except Anggota.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page. Please wait for the admin to assign you to an RT/RW."})
    try:
        pengurus = Pengurus.objects.get(anggota=anggota)
    except Pengurus.DoesNotExist:
        pengurus = None
    
    listKegiatan = Kegiatan.objects.order_by("waktuKegiatan")[:5]
    context = {
        "listKegiatan": listKegiatan,
        "pengurus": pengurus,
        "role": request.session['role']
    }
    return render(request, "agenda/index.html", context)

@login_required(login_url='/auth/login/')
def detail(request, kegiatan_id):
    kegiatan = Kegiatan.objects.get(id__exact=kegiatan_id)
    context = {
        "kegiatan" : kegiatan,
    }
    return render(request, "agenda/detail.html", context)

@login_required(login_url='/auth/login/')
def add_kegiatan(request):
    if not request.user.is_authenticated:
        return render(request, 'unauthenticated_access.html')
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthenticated_access.html')
    try:
        anggota = Anggota.objects.get(pengguna=pengguna)
    except Anggota.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page. Please wait for the admin to assign you to an RT/RW."})
    try:
        pengurus = Pengurus.objects.get(anggota=anggota)
    except Pengurus.DoesNotExist:
        return render(request, 'agenda/add_kegiatan_unauthorized_access.html', {'info': "You don't have access to this page. This page can only be accesed by Pengurus."})
    
    if request.method == 'POST':
        form = KegiatanForm(request.POST)
        if form.is_valid():
            # create a new `Kegiatan` and save it to the db
            new_kegiatan = form.save(commit=False)
            new_kegiatan.pengurus = pengurus
            new_kegiatan.save()
            return redirect("agenda:index")

    else:
        form = KegiatanForm()
            
    return render(request,
                'agenda/add_kegiatan.html',
                {'form': form})
