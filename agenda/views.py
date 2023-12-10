from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Kegiatan
from .forms import KegiatanForm

@login_required(login_url='/auth/login/')
def index(request):
    listKegiatan = Kegiatan.objects.order_by("waktuKegiatan")[:5]
    context = {
        "listKegiatan": listKegiatan,
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
    if request.method == 'POST':
        form = KegiatanForm(request.POST)
        if form.is_valid():
            # create a new `Kegiatan` and save it to the db
            kegiatan = form.save()
            return redirect("agenda:detail", kegiatan.id)

    else:
        form = KegiatanForm()
            
    return render(request,
                'agenda/add_kegiatan.html',
                {'form': form})
