from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Layanan
from .forms import LayananForm


# Create your views here.
@csrf_exempt
@login_required(login_url='/auth/login/')
def show_all_layanan(request):
    query = request.GET.get('q')
    active = request.GET.get('active')
    role = request.session['role']

    layanan = Layanan.objects.all()

    if len(layanan) > 0:
        if query:
            layanan = layanan.filter(Q(nama__icontains=query))
        if active:
            today = timezone.now().date()
            layanan = layanan.filter(Q(end_date__gte=today))

    if request.method == 'GET':
        # user is validated
        if role == 'P' or role == 'A':
            context = {
                'role': role,
                'layanan': layanan
            }
            return render(request, 'layanan.html', context)
        else:
            # render unauthorized page, wait for verification from admin (assign rw & rt)
            return render(request, 'unauthorized.html')


@csrf_exempt
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



