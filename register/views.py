from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib import messages

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'register/logout.html', {'title':'Logout'})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthenticationForm()
            message = 'You have been succesfully signed'
            return render(request, 'registration/login-view.html', {'title':'Login','form':form, 'message':message})
        else:
            for error_message in form.errors.items():
                message = error_message[1][0]
                return render(request, 'register/register.html', {'form':form ,'title':'Register','message':message})
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form':form ,'title':'Register'})

def login_view(request):
    form = AuthenticationForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            message = 'Invalid username or password'
            return render(request, 'registration/login-view.html', {'title':'Login','form':form, 'message':message})
    return render(request, 'registration/login-view.html', {'title':'Login','form':form})