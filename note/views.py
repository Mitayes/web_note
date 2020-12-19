from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.http import JsonResponse



def index(request):
    return render(request, 'index.html', {'test': 'test text'})


def auth(request):
    return render(request, 'auth.html', {'test': 'test text'})


def register(request):
    return render(request, 'register.html', {'test': 'test text'})


def note_create(request):
    return render(request, 'note_create.html', {'test': 'test text'})


def note_list(request):
    return render(request, 'note_list.html', {'test': 'test text'})
