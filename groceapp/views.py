from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.forms import groceform
from django.contrib.auth.models import User

# Create your views here.



def userform(request):
    if request.method=='POST':
        form=groceform(request.POST)
        if form.is_valid():
            form.save()
            print('user registered')
            return HttpResponseRedirect('home')
    else:
        form=groceform()    
        return render(request,'reg.html',{'form':form})
            
        
    
    
def gg(request):
    return render(request,'gg.html')