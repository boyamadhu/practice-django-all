from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufo1=UserForm(request.POST)
        pfo1=ProfileForm(request.POST,request.FILES)
        if ufo1.is_valid() and pfo1.is_valid():
            ufo2=ufo1.save(commit=False)
            ufo2.set_password(ufo1.cleaned_data['password'])
            ufo2.save()
            pfo2=pfo1.save(commit=False)
            pfo2.username=ufo2
            pfo2.save()
            return HttpResponse('data is inserted succesfully')
        else:
            return HttpResponse('data is not valid')

    return render(request,'register.html',d)