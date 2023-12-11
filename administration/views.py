from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from authentication.models import Pengguna
from .forms import PenggunaUpdateForm, AnggotaForm, PengurusForm
from .models import Anggota, Pengurus

# Create your views here.

@csrf_exempt
@login_required(login_url='/auth/login/')
def update_profile(request):
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthenticated_access.html')
    

    if request.method == 'POST':
        pengguna_form = PenggunaUpdateForm(request.POST, request.FILES, instance=pengguna)
        if pengguna_form.is_valid():
            pengguna_form.save()

            return render(request, 'view_profile.html', {'pengguna': pengguna})
    else:
        pengguna_form = PenggunaUpdateForm(instance=pengguna)

    return render(request, 'update_profile.html', {'pengguna_form': pengguna_form})


@csrf_exempt
@login_required(login_url='/auth/login/')
def view_profile(request):
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthenticated_access.html')

    try:
        anggota = Anggota.objects.get(pengguna=pengguna)
    except Anggota.DoesNotExist:
        anggota = None

    try:
        pengurus = Pengurus.objects.get(anggota = anggota)
    except Pengurus.DoesNotExist:
        pengurus = None

        
    return render(request, 'view_profile.html', {'pengguna': pengguna, 'anggota': anggota, 'pengurus':pengurus})


@csrf_exempt
def create_superuser(request):
    User.objects.create_superuser('testadmin', 'admin@admin.com', 'rukunchat')
    return redirect('authentication:index')
