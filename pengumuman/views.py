from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from authentication.models import Pengguna

from .models import Pengumuman
from .forms import PengumumanForm

def pengumuman_list(request):
    pengumumans = Pengumuman.objects.all()
    form = PengumumanForm()

    if request.method == 'POST':
        form = PengumumanForm(request.POST)
        if form.is_valid():
            new_pengumuman = form.save(commit=False)
            new_pengumuman.user = Pengguna.objects.get(user=request.user)
            new_pengumuman.save()
            return redirect('pengumuman:pengumuman_list')

    return render(request, 'pengumuman_list.html', {'pengumumans': pengumumans, 'form': form})

def pengumuman_detail(request, id):
    pengumuman = get_object_or_404(Pengumuman, id=id)
    return render(request, 'pengumuman_detail.html', {'pengumuman': pengumuman})