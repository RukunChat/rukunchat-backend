from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Layanan
from .forms import LayananForm


# Create your views here.
@login_required(login_url='/auth/login/')
def show_all_layanan(request):
    query = request.GET.get('q')
    active = request.GET.get('active')
    print('afmwioepf')
    layanan = Layanan.objects.all()

    if query:
        layanan = layanan.filter(Q(nama__icontains=query))
    if active:
        print('active')
        today = timezone.now().date()
        layanan = layanan.filter(Q(end_date__gte=today))

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



