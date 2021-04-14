from django import forms
from .models import Paste, Language

choices = Language.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)
    
class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ('title', 'language', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your title for paste'}),
            'language': forms.Select(choices= choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This place add your content'}),
        }