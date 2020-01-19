from django.shortcuts import render

def index(request):
    return render(request, 'sets/index.html')