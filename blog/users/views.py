# Renderring is to display html templates.
# Redirecting to other urls.
from django.shortcuts import render, redirect
# Importing form from inbuilt django User Creation Forms.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# User Logging In
from django.contrib.auth import login, logout

# Create your views here.
def signup_func(request):
    # checking for the type of the request.
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Saving the form info in user and using this user variable to login automatically.
            user = form.save()
            login(request, user)
            return redirect('article:arlist')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form':form})

def login_func(request):
    # checking for the type of the request.
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('article:arlist')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def logout_func(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article:arlist')
