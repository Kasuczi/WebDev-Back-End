from django import forms
from .models import Comment


class PythonistForm(forms.Form):
    name = forms.CharField(label='Twoje imie', max_length=30)
    birth_date = forms.DateField(label='Data Urodzenia')
    email = forms.EmailField(label='E-mail', required=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
