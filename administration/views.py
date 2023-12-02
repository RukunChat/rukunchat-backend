from django.shortcuts import render, redirect

from authentication.models import Pengguna
from .forms import PenggunaUpdateForm, AnggotaForm, PengurusForm
from .models import Anggota, Pengurus

# Create your views here.
def update_profile(request):

    pengguna = Pengguna.objects.get(user=request.user)
    

    if request.method == 'POST':
        pengguna_form = PenggunaUpdateForm(request.POST, request.FILES, instance=pengguna)
        if pengguna_form.is_valid():
            pengguna_form.save()

            # Check if the user is signing up as Pengurus
            if request.POST.get('is_pengurus'):
                anggota_form = AnggotaForm(request.POST)
                pengurus_form = PengurusForm(request.POST)
                
                if anggota_form.is_valid() and pengurus_form.is_valid():
                    anggota = anggota_form.save(commit=False)
                    anggota.pengguna = pengguna
                    anggota.save()

                    pengurus = pengurus_form.save(commit=False)
                    pengurus.anggota = anggota
                    pengurus.save()

            return redirect('profile')  # Change 'profile' to your profile page URL
    else:
        pengguna_form = PenggunaUpdateForm(instance=pengguna)

    return render(request, 'update_profile.html', {'pengguna_form': pengguna_form})