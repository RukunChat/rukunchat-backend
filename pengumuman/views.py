from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from authentication.models import Pengguna

from .models import Pengumuman
from .forms import PengumumanForm

def pengumuman_list(request):
    query = request.GET.get('q')
    order_by = request.GET.get('order_by', '-date_created')
    pengumumans = Pengumuman.objects.all().order_by(order_by)  
    topic = request.GET.get('topic')  
    if query:
        pengumumans = pengumumans.filter(Q(title__icontains=query))

    if topic:
        pengumumans = pengumumans.filter(Q(topic=topic))

    form = PengumumanForm()

    if request.method == 'POST':
        form = PengumumanForm(request.POST)
        if form.is_valid():
            new_pengumuman = form.save(commit=False)
            new_pengumuman.user = Pengguna.objects.get(user=request.user)
            new_pengumuman.save()
            return redirect('pengumuman:pengumuman_list')

    return render(request, 'pengumuman_list.html', {'pengumumans': pengumumans, 'form': form, 'topic': topic})

def pengumuman_detail(request, id):
    pengumuman = get_object_or_404(Pengumuman, id=id)
    return render(request, 'pengumuman_detail.html', {'pengumuman': pengumuman})
