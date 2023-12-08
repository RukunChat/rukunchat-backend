from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Pengguna
from .forms import SignupForm


def index(request):
    return render(request, 'landingPage.html')

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
        context = {'form': form}
        return render(request, 'signup.html', context)
    
    elif request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        form = SignupForm(request.POST, request.FILES)  # Add request.FILES for file uploads

        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            nama_lengkap = form.cleaned_data['nama_lengkap']
            tgl_lahir = form.cleaned_data['tgl_lahir']
            alamat = form.cleaned_data['alamat']
            nik = form.cleaned_data['nik'] if 'nik' in form.cleaned_data else None

            pengguna = Pengguna.objects.create(
                user=user,
                nama_lengkap=nama_lengkap,
                tanggal_lahir=tgl_lahir,
                alamat=alamat,
                nik=nik,
                active=False
            )
            
            pengguna.save()

            return render(request, 'login.html')

    # If the form is not valid, return the form and display errors
    context = {'form': form}
    return render(request, 'signup.html', context)



