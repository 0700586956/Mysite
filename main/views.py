from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Tutorial, Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import PersonForm


# Create your views here.
#Rendering data form database
def person_details_view(request):
    obj = Person.objects.all()
    # context = {
    #     'name': obj.name,
    #     'location': obj.location
    # }
    context = {
        'object': obj
    }
    return render(request, "main/person_details.html", context)

#For creating person
def person_create_view(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
         savereq=Person(name=request.POST['name'],location=request.POST['location'])
         form.save()
    else:
        form=PersonForm() 
        context = {
            'form':form
        }
    form =PersonForm
    return render(request, "main/person_create.html",context={"form":form})
    

#For home page
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all})
#Registering new user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "New Account Created: {username} ")
            login(request, user)
            messages.info(request, "You are logged in as {username} ")            
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, "{msg}: {from.error_messages")
                

    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context={"form":form})