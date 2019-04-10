from django.shortcuts import render, redirect


def index(request):
    pass
    return render(request, 'driver/index.html')


def login(request):
    pass
    return render(request, 'driver/login.html')


def register(request):
    pass
    return render(request, 'driver/register.html')


def logout(request):
    pass
    return redirect("/index/")

