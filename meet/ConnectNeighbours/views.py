from .forms import PersonForm
from django.shortcuts import render,redirect
from .models import Person
# Create your views here.

def greet(request):
    return render(request,'greet.html')

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/meet')
    else:
        form = PersonForm()
    
    return render(request,'index.html',{'form':form});


def meet(request):
    people=Person.objects.all();
    return render(request,'people.html',{'people':people})

def sort(request):
    people=Person.objects.all();
    return render(request,'sort.html',{'people':people})

def sortbyage(request,age):
    people=Person.objects.filter(Age=age)
    return render(request,'sort.html',{'people':people})   
def sortgender(request,sex):
    people=Person.objects.filter(Gender=sex)
    return render(request,'sort.html',{'people':people})    

def teenage(request):
    people=Person.objects.filter(Age__lt=18)
    return render(request,'sort.html',{'people':people})    

def adults(request):
    people=Person.objects.filter(Age__gt=18)
    return render(request,'sort.html',{'people':people})   


def events(request):
    return render(request,'events.html') 
