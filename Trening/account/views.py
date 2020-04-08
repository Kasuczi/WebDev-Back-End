from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LogInForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnianie pomyślne')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane')
    else:
        form = LogInForm()
    return render(request, 'account/login.html', {'form': form})


def my_account(request):
    return render(request, 'account/my_account.html')


def log_out(request):
    logout(request)
    return HttpResponse('wylogowano')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home_page')
    template_name = 'account/signup.html'
