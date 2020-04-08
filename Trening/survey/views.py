from django.shortcuts import render
from .forms import SurveyForm

# Create your views here.

def send_survey(request):
    cd = False
    if request.method == 'GET':
        form = SurveyForm()
    else:
        form = SurveyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    return render(request, 'survey/survey.html',
                  {'form':form, 'data': cd})