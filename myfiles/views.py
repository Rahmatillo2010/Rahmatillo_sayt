from django.shortcuts import render
from myfiles.models import *
# Create your views here.
import datetime

def index(malumot):
    ishlarimiz = Portfolio.objects.all()
    servis = Services.objects.all()
    team = Team.objects.all()
    if 'id' in malumot.POST:
        email = malumot.POST.get('id')
        Subr(email=email, date=datetime.datetime.now()).save()
    elif malumot.method=="POST":
        name = malumot.POST.get('name')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        Malumot_saqlash(name=name,email=email,subject=subject,message=message,date=datetime.datetime.now()).save()
    return render(malumot,'index.html', {"works": ishlarimiz,"wors":servis, "wosr":team})

def inner(malumot):
    return render(malumot,'inner-page.html')

def qoshish(malumot):
    return render(malumot,'index.html')


def services(malumot):
    ishlarimiz = Services.objects.all()
    return render(malumot,'index.html', {"wors": ishlarimiz})


def por(malumot,id):
    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html', {"work":ishlarimiz})