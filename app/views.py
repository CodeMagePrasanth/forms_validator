from django.shortcuts import render

from app.forms import *

from django.http import HttpResponse

def student(request):
    SFO = Studentform()
    d = {'SFO' : SFO}

    if request.method == 'POST':
        SFDO = Studentform(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invaild Data')

    return render(request,'student.html',d)