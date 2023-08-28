from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Register your models here.
def Insert_Topic(request):
       rk=input('Enter topic_name: ')
       to=topic.objects.get_or_create(topic_name=rk)[0]
       to.save()
       return HttpResponse("DATE entry")
def Insert_webpage(request):
       rk=input('Enter topic_name:')
       to=topic.objects.get_or_create(topic_name=rk)[0]
       to.save()
       n=input('Enter name: ')
       u=input('enter url: ')
       wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
       wo.save()
       return HttpResponse("DATA entry")
def Insert_Access(request):
       tn = input('enter topic_name:')
       rk=input('Enter name:') 
       
       u=input('enter url: ')

       to=topic.objects.get_or_create(topic_name=tn)[0]
       to.save()
       wo=webpage.objects.get_or_create(topic_name=to,name=rk,url=u)[0]
       wo.save()
       d=input('Enter date: ')
       a=input('Enter author: ')
       ao=accessrecords.objects.get_or_create(name=wo,date=d,author=a)[0]
       ao.save()
       return HttpResponse("DATA entry")