from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('proyecto_list')
    else:
        form = UserCreationForm()
    return render(request, 'documentation_app/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('proyecto_list')
    else:
        form = AuthenticationForm()
    return render(request, 'documentation_app/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login')