from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_student(request):
    SFEO=Studentform()
    d={'SFEO':SFEO}


    if request.method=='POST':
        SFD=Studentform(request.POST)
        if SFD.is_valid():
            Sname=SFD.cleaned_data['Sname']
            Sid=SFD.cleaned_data['Sid']
            Semail=SFD.cleaned_data['Semail']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
            return HttpResponse('Student data is successfully inserted')


        
    return render(request,'insert_student.html',d)