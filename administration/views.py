from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Pengguna
from .forms import PenggunaUpdateForm, AnggotaForm, PengurusForm
from .models import Anggota, Pengurus

# Create your views here.
@login_required(login_url='/auth/login/')
def update_profile(request):

    pengguna = Pengguna.objects.get(user=request.user)
    

    if request.method == 'POST':
        pengguna_form = PenggunaUpdateForm(request.POST, request.FILES, instance=pengguna)
        if pengguna_form.is_valid():
            pengguna_form.save()

            return render(request, 'view_profile.html', {'pengguna': pengguna})
    else:
        pengguna_form = PenggunaUpdateForm(instance=pengguna)

    return render(request, 'update_profile.html', {'pengguna_form': pengguna_form})

@login_required(login_url='/auth/login/')
def view_profile(request):
    pengguna = Pengguna.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'pengguna': pengguna})

# #            <a href="{% url 'register_anggota' %}" class="btn btn-success">Register as Anggota RT RW</a>
#             <a href="{% url 'register_pengurus' %}" class="btn btn-warning">Register as Pengurus RT/RW</a>