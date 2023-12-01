from django.shortcuts import render
from django.http import HttpResponse

from .models import Pengumuman

def pengumuman_list(request):
    pengumumans = Pengumuman.objects.all()
    return render(request, 'pengumuman_list.html', {'pengumumans': pengumumans})
