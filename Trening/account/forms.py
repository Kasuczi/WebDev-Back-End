from django import forms
from django.core.exceptions import ValidationError


def validate_ends_with_a(value):
    if not value.endswith('a'):
        raise ValidationError('nazwa uzytkownika musi'
                              ' konczyc sie na a')

class LogInForm(forms.Form):
    username = forms.CharField(validators=[validate_ends_with_a])
    password = forms.CharField(widget=forms.PasswordInput)