from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title', 'topic')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'}),
        }
