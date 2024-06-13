from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    today = datetime.today()
    return render(request, 'home.html', {'today': today})

@login_required(login_url='/userLogin')
def authorized(request):
    return render(request, 'authorized.html', {})

def userLogin(request):
    return render(request, 'userLogin.html', {})

def UserLogin(request, id):
    return render(request, 'userLogin.html', {'id':id})