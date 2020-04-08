from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('signup/', views.SignUp.as_view(), name='signup')
]

