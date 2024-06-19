from django.shortcuts import render

# Create your views here.
def News(request):
    return render(request, 'news.html')