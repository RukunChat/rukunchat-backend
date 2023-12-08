# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    nama_lengkap = forms.CharField(max_length=255)
    tgl_lahir = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    alamat = forms.CharField()
    nik = forms.IntegerField(required=False, min_value=1000000000000000, max_value=9999999999999999)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'nama_lengkap', 'tgl_lahir', 'alamat', 'nik')
