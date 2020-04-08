from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


def validate_div_3(value):
    if value % 3 != 0:
        raise ValidationError(f'liczba {value} nie jest podzielna '
                              f'przez 3')


class MultiEmailField(forms.Field):
    def to_python(self, value):
        print('### to_python(', value, ")")
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        for email in value:
            validators.validate_email(email)


class SurveyForm(forms.Form):
    FRAMEWORK_CHOICES = (enumerate(['Django', 'Flask', 'Tornado', 'Pylon']))
    PYTHON_CHOICES = (enumerate(['v2', 'v3']))
    name = forms.CharField(label='imie',
                           validators=[validators.MaxLengthValidator(10)])
    birth_date = forms.DateField(label='data urodzenia',
                                 widget=forms.SelectDateWidget())
    password = forms.CharField(label='haslo', widget=forms.PasswordInput)
    post_code = forms.RegexField(regex=r'\d{2}\-\d{3}')
    python = forms.CharField(label='wersja pythona',
                             widget=forms.RadioSelect(choices=PYTHON_CHOICES))
    hobby = forms.MultipleChoiceField(choices=FRAMEWORK_CHOICES,
                                      label='Hobby',
                                      widget=forms.CheckboxSelectMultiple)
    recipients = MultiEmailField(label='odbiorcy maila')
    number = forms.IntegerField(label='ulubiona liczba', validators=[validate_div_3])
