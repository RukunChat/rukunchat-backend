from django import forms
from .models import Layanan


class LayananForm(forms.ModelForm):
    nama = forms.CharField(max_length=255)
    deskripsi = forms.CharField(max_length=255)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Layanan
        fields = ('nama', 'deskripsi', 'start_date', 'end_date')