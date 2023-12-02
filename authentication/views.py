from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Pengguna
from .forms import SignupForm


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/login/')
def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('/auth/login/')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # TODO: redirect to landing page
            return render(request, 'landingPage.html')

def user_signup(request):
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

            pengguna = Pengguna.objects.create(
                user=user,
                nama_lengkap=nama_lengkap,
                tanggal_lahir=tgl_lahir,
                alamat=alamat,
                nik=nik,
                foto=foto,
                active=False
                )
            
            pengguna.save()

            return render(request, 'index.html', {})



