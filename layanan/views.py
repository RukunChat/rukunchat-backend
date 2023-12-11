from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Layanan
from .forms import LayananForm

from administration.models import Pengguna, Anggota, RT, RW


# Create your views here.
@csrf_exempt
@login_required(login_url='/auth/login/')
def show_all_layanan(request):
    query = request.GET.get('q')
    active = request.GET.get('active')
    role = request.session['role']

    if request.method == 'GET':
        # user is validated
        if role == 'P' or role == 'A':
            rw = resolve_rw(request)
            layanan = Layanan.objects.filter(RW=rw)
            
            if len(layanan) > 0:
                if query:
                    layanan = layanan.filter(Q(nama__icontains=query))
                if active:
                    today = timezone.now().date()
                    layanan = layanan.filter(Q(end_date__gte=today))

            context = {
                'local': f'RW {rw.nomor}, {rw.kecamatan}, {rw.kabupaten}.',
                'role': role,
                'layanan': layanan
            }
            return render(request, 'layanan_list.html', context)
        
        else:
            # render unauthorized page, wait for verification from admin (assign rw & rt)
            return render(request, 'layanan_unauthorized.html')


@csrf_exempt
@login_required(login_url='/auth/login/')
def add_layanan(request):

    if request.method == 'GET':
        form = LayananForm()
        context = {
            'form': form
        }
        return render(request, 'layanan_add.html', context)
    
    elif request.method == 'POST':
        form = LayananForm(request.POST)
        if form.is_valid():
            layanan = form.save(commit=False)
            print(layanan)
            rw = resolve_rw(request)
            layanan.RW = rw 
            layanan.save()
            return redirect('layanan:show_all_layanan')
        

def resolve_rw(request):
    '''
    returns current user's rw
    '''
    pengguna = Pengguna.objects.get(user=request.user)
    anggota = Anggota.objects.get(pengguna=pengguna)

    rt = anggota.RT
    rw = rt.RW

    return rw

