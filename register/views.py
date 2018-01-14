from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("hi")



