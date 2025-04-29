from django import forms
from .models import TheBookLost
from markdownx.fields import MarkdownxFormField

class TheBookLostForm(forms.ModelForm):
    class Meta:
        model = TheBookLost
        fields = ['title', 'content']
