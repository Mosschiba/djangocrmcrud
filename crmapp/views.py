from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # check if authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You logged in seccefully..!')
            return redirect('home')
        else:
            messages.success(
                request, 'there was some thing wrong, Please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged Out.')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
