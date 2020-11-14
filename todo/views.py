from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

# Create your views here.

def home(request):
	return render(request, 'todo/home.html')


def signupuser(request):
	if request.method == 'GET':
		return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
	else:
		#auth model created user data.
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request, user)#to login as new user after registration
				redirect('currenttodos')#to goto the todos page after login
			except IntegrityError:
				return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error':'That username has already been taken.Please choose a new username'})
		else:
			#print("Password's didn't match")
			return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

			
def currenttodos(request):
	return render(request,'todo/currenttodos.html')