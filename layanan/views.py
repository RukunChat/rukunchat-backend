from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Layanan
from .forms import LayananForm


# Create your views here.
@login_required(login_url='/auth/login/')
def show_all_layanan(request):
    layanan = Layanan.objects.all()

    if request.method == 'GET':
        context = {
            'layanan': layanan
        }
        return render(request, 'layanan.html', context)
    
@login_required(login_url='/auth/login/')
def add_layanan(request):

    if request.method == 'GET':
        form = LayananForm()
        context = {
            'form': form
        }
        return render(request, 'add_layanan.html', context)
    
    elif request.method == 'POST':
        layanan = LayananForm(request.POST)
        if layanan.is_valid():
            layanan.save()
            return redirect('layanan:show_all_layanan')



