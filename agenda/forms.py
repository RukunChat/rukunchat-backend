from django import forms

from .models import Kegiatan

class KegiatanForm(forms.ModelForm):
  class Meta:
    model = Kegiatan
    fields = ['namaKegiatan', 'deskripsiKegiatan', 'waktuKegiatan']
    widgets = {
            'waktuKegiatan': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }