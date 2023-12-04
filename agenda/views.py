from django.shortcuts import render
from django.http import HttpResponse

from .models import Kegiatan

def index(request):
    listKegiatan = Kegiatan.objects.order_by("waktuKegiatan")[:5]
    context = {
        "listKegiatan": listKegiatan,
    }
    return render(request, "index.html", context)

def detail(request, kegiatan_id):
    return HttpResponse("You're looking at agenda %s." % kegiatan_id)