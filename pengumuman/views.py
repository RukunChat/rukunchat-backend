from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from administration.models import Anggota, Pengurus
from authentication.models import Pengguna

from .models import Pengumuman
from .forms import PengumumanForm

@csrf_exempt
def pengumuman_list(request):
    if not request.user.is_authenticated:
        return render(request, 'unauthenticated_access.html')
    
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page because you are not part of this organization"})

    try:
        anggota = Anggota.objects.get(pengguna=pengguna)
    except Anggota.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page. Please wait for the admin to assign you to an RT/RW."})


    query = request.GET.get('q')
    order_by = request.GET.get('order_by', '-date_created')
    pengumumans = Pengumuman.objects.filter(anggota__RT__RW=anggota.RT.RW).order_by(order_by)  
    topic = request.GET.get('topic')  
    rt_filter = request.GET.get('rt_filter')

    if query:
        pengumumans = pengumumans.filter(Q(title__icontains=query))

    if topic:
        pengumumans = pengumumans.filter(Q(topic=topic))

    if rt_filter:
        pengumumans = pengumumans.filter(Q(anggota__RT__nomor=rt_filter))

    form = PengumumanForm()

    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            new_pengumuman = form.save(commit=False)
            new_pengumuman.anggota = anggota
            new_pengumuman.save()
            return redirect('pengumuman:pengumuman_list')

    return render(request, 'pengumuman_list.html', {'pengumumans': pengumumans, 'form': form, 'topic': topic, 'anggota': anggota, 'role': request.session['role'], 'rt_filter': rt_filter})


@csrf_exempt
def pengumuman_detail(request, id):
    if not request.user.is_authenticated:
        return render(request, 'unauthenticated_access.html')
    
    try:
        pengguna = Pengguna.objects.get(user=request.user)
    except Pengguna.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page. Please wait for the admin to assign you to an RT/RW."})

    try:
        anggota = Anggota.objects.get(pengguna=pengguna)
    except Anggota.DoesNotExist:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page. Please wait for the admin to assign you to an RT/RW."})

    pengumuman = get_object_or_404(Pengumuman, id=id)
    if pengumuman.anggota.RT.RW != anggota.RT.RW:
        return render(request, 'unauthorized_access.html', {'info': "You don't have access to this page because you are not part of this organization"})
    return render(request, 'pengumuman_detail.html', {'pengumuman': pengumuman, 'anggota': anggota, 'role': request.session['role']})
