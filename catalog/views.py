from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 

from django.http import HttpResponse

from .form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import  User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def login_user(request):
    if request.method =="POST":
        #form =LoginForm(request.POST)
        form =NewUserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
            username= cd['username'],
            password = cd['password'])

            if user is not None:
               login(requst, user)
               return HttpResponse('authentification was successfull')

            else:
              return HttpResponse('authentification failed, please try again')
    else:

        #form = LoginForm()
        form = NewUserForm()
    return render(request=request, template_name='login.html',context= {'form':form})   


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name ="register.html", context={'register_form':form} )
def index (request):
	return render(request, 'home.css')

def dietreq(request):
    return render(request, 'dietreq.html')
