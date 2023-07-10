from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        print(tn)
        TO=topic.objects.create(topic_name=tn)
        TO.save()
        return HttpResponse('dfghjkl')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    TO=topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        email=request.POST['email']
        date=request.POST['date']
        TO1=topic.objects.get_or_create(topic_name=tn)[0]
        TO1.save()
        TO3=Webpage.objects.get_or_create(topic_name=TO1,name=n,email=email,date=date)[0]
        TO3.save()
        return HttpResponse('dfghjkl')
    return render(request,'insert_webpage.html',d)

def retrieve_topic(request):
    TO=topic.objects.all()
    d={'topics':TO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        new=Webpage.objects.none()

        for i in tn:
            new=new | Webpage.objects.filter(topic_name=i)

        d1={'topics':new}
        return render(request,'retrieve_topic.html',d1)
    return render(request,'retrieve_topics.html',d)