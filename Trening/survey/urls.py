from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.send_survey, name= 'send_survey')
]