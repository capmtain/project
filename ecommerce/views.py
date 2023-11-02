from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.forms import groceform
from.models import category,properties,cars,UserProfile,bikes,mobile,Electronics,Furniture
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.views.generic import DetailView,CreateView,ListView,UpdateView,DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
# Create your views here.





# def log(request):
#     return render(request,'log.html')
# def  fr(request):
#     if request.method=='POST':
#         form=Fruit(request.POST)
#         if form.is_valid():
#            form.save
#            return redirect('/')
#     else:
#         form=Fruit
#         return render(request,'groce.html')
def home(request):
    return render (request,'home.html')


def log(request):
    return render (request,'login.html')

def userform(request):
    if request.method=='POST':
        form=groceform(request.POST)
        if form.is_valid():
            form.save()
            print('user registered')
            return redirect('/ecommerce')
        else:
            HttpResponseRedirect('both password must be same')
    else:
        form=groceform()    
        return render(request,'reg.html',{'form':form})
    
def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.object.get(username=username)
            
        except:
            print('error')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/ecommerce/')
    else:
        return render(request,'groform.html')
    
def logoutpage(request): 
    logout(request)
    print('user logout')
    return redirect('/ecommerce')
def categories(request):
    cat=category.objects.all()
    return render (request,'category.html',{'cat':cat})
def property(request):
    prop=properties.objects.all()
    return render(request,'properties.html',{'prop':prop})
def car(request):
    car=cars.objects.all()
    return render(request,'cars.html',{'car':car})
def mobiles(request):
    mob=mobile.objects.all()
    return render(request,'mobile.html',{'mob':mob})
def bike(request):
    bik=bikes.objects.all()
    return render(request,'bikes.html',{'bik':bik})
def electronics(request):
    ele=Electronics.objects.all()
    return render(request,'elect.html',{'ele':ele})
def furnitures(request):
    fur=Furniture.objects.all()
    return render(request,'fur.html',{'fur':fur})

class detail(DetailView):
    model=properties
   
    context_object_name="dt"
    template_name="detail.html"
    
class deta(DetailView):
    model=cars
   
    context_object_name="dt"
    template_name="detail.html"
class deta1(DetailView):
    model=Furniture
   
    context_object_name="dt"
    template_name="detail.html"
class deta2(DetailView):
    model=Electronics
   
    context_object_name="dt"
    template_name="detail.html"
class deta3(DetailView):
    model=bikes
   
    context_object_name="dt"
    template_name="detail.html"
class deta4(DetailView):
    model=mobile
   
    context_object_name="dt"
    template_name="detail.html"



def search(request):
    search=''
    if request.GET.get('search'):
        search=request.GET.get('search')
        print('search')
    sr=properties.objects.filter(Q(addr__icontains=search)|Q(image__icontains=search)|Q(des__icontains=search)|Q(price__icontains=search))
#    sd=cars.objects.filter(Q(detail__icontains=search)|Q(image__icontains=search)|Q(des__icontains=search)|Q(price__icontains=search))
    return render(request,'search.html',{'sr':sr})
def search1(request):
    search=''
    if request.GET.get('search'):
        search=request.GET.get('search')
        print('search')
    # sr=properties.objects.filter(Q(addr__icontains=search)|Q(image__icontains=search)|Q(des__icontains=search)|Q(price__icontains=search))
    sd=cars.objects.filter(Q(detail__icontains=search)|Q(image__icontains=search)|Q(des__icontains=search)|Q(price__icontains=search))
    return render(request,'search.html',{'sd':sd})
class create(CreateView):
    template_name='create.html'
    model=UserProfile
    fields='__all__'
    success_url=reverse_lazy('create')
class list(ListView):
    template_name='list.html'
    model=UserProfile
    context_object_name='list'



class update(UpdateView):
    template_name='create.html'
    model=UserProfile
    fields='__all__'
    success_url=reverse_lazy('/')

class delete(DeleteView):
    template_name='delete.html'
    model=UserProfile
    context_object_name='del'
    success_url=reverse_lazy('/')   



# def enter(request):
#     if request.method=='POST':
#       return HttpResponseRedirect('submitted')   
#     return render(request,'enter.html')
    




