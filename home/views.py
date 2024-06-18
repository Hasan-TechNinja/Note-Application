from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import calculator

# Create your views here.
def home(request):
    today = datetime.today()
    return render(request, 'home.html', {'today': today})

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/userLogin')
def authorized(request):
    return render(request, 'authorized.html', {})

def userLogin(request):
    return render(request, 'userLogin.html', {})

def UserLogin(request, id):
    return render(request, 'userLogin.html', {'id':id})

def Calculator(request):
    cal = calculator()
    result = 0
    try:
        if request.method == "POST":
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operator = request.POST.get('operator')
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
    except:
        pass

    return render(request, 'calculator.html', {'result': result, 'calculator': cal })

def result(request):
    return render(request, 'result.html')