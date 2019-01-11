# Renderring is to display html templates.
# Redirecting to other urls.
from django.shortcuts import render, redirect
# Importing form from inbuilt django User Creation Forms.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# User Logging In
from django.contrib.auth import login, logout

def signup_func(request):
    print(1)
    if request.method == 'POST':
        print(2)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(3)
            user = form.save()
            return redirect('article:arlist')
    else:
        print(4)
        form = UserCreationForm()
    print(9)
    return render(request, 'users/signup.html', {'form':form})

def signin_func(request):
    print(5)
    if request.method == 'POST':
        print(6)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(7)
            user = form.get_user()
            login(request, user)
            return redirect('article:arlist')
    else:
        print(8)
        form = AuthenticationForm()
    print(10)
    return render(request, 'users/signin.html', {'form':form})

def signout_func(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article:arlist')
