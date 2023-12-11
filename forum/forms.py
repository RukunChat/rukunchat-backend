from django import forms
from .models import Forum, ForumResponse

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title', 'topic')

class ForumResponseForm(forms.ModelForm):
    class Meta:
        model = ForumResponse
        fields = ('response_text',)
