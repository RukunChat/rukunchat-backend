# authentication/forms.py
from django import forms
from .models import Pengguna
from .models import Anggota, Pengurus

class PenggunaUpdateForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = ['nama_lengkap', 'tanggal_lahir', 'alamat', 'nik', 'foto', 'active']

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['RT']

class PengurusForm(forms.ModelForm):
    class Meta:
        model = Pengurus
        fields = ['jabatan']