from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, login


def home(request):
    return render(request, 'foo/home.html')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

