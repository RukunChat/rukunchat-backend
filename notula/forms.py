from django import forms
from .models import Notula

class NotulaForm(forms.ModelForm):
    class Meta:
        model = Notula
        fields = ['title', 'topik', 'poinpembahasan', 'hasilrapat', 'lokasirapat']