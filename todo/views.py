from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo

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
				return redirect('currenttodos')#to goto the todos page after login
			except IntegrityError:
				return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error':'That username has already been taken.Please choose a new username'})
		else:
			#print("Password's didn't match")
			return render(request,'todo/signupuser.html',{'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
	if request.method == 'GET':
		return render(request,'todo/loginuser.html',{'form':AuthenticationForm()})
	else:
		user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request,'todo/loginuser.html',{'form':AuthenticationForm(),'error':'Username and password did not match'})
		else:
			login(request, user)
			print("after login")
			return redirect('currenttodos')
			print("after rediret")
			
def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

			
def currenttodos(request):
	todos = Todo.objects.filter(user=request.user,datecompleted__isnull=True) #Todo.objects.all()
	return render(request,'todo/currenttodos.html',{'todos':todos})

def createtodo(request):
	if request.method=='GET':
		return render(request,'todo/createtodo.html',{'form':TodoForm()})
	else:
		try:
			form = TodoForm(request.POST)
			newtodo = form.save(commit=False)#Falsemeans not tosave in db yet
			newtodo.user=request.user
			newtodo.save()
			return redirect('currenttodos')
		except ValueError:
			return render(request, 'todo/createtodo.html', {'form': TodoForm(),'error':'Bad data passed in'})
