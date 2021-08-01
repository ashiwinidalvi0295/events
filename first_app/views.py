
from django.shortcuts import render,redirect
from first_app.forms import Addeventsform
from django.http import HttpResponse
from first_app.models import events
# Create your views here.
def index(request):
    return HttpResponse('Hello World! This is my First Django Page! Welcome!!!')
# Create your views here.
def add_events_view(request):
    form=Addeventsform()
    if request.method=='POST':
        form=Addeventsform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Addeventsform()

    return render(request,'add_events.html',{'form':form})

def read_events_view(request):
    data=events.objects.all()
    return render(request,'first_app/read_events.html',{'data':data})
