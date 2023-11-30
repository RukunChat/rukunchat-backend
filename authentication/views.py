from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Pengguna
from .forms import SignupForm


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        pengguna = Pengguna.objects.get(user=user)
        if pengguna is not None:
            login(request, user)
            return render(request, '200.html')

def signup(request):
    form = SignupForm()
    
    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)
    
    elif request.method == 'POST':
        user = UserCreationForm(request.POST)

        if user.is_valid():
            user = user.save()
            nama_lengkap = request.POST['nama_lengkap']
            tgl_lahir = request.POST['tgl_lahir']
            alamat = request.POST['alamat']
            nik = request.POST['nik']
            foto = request.POST['foto']

            Pengguna.objects.create(
                user=user,
                nama_lengkap=nama_lengkap,
                tanggal_lahir=tgl_lahir,
                alamat=alamat,
                nik=nik,
                foto=foto,
                active=False
                )

            return render(request, 'index.html', {})



