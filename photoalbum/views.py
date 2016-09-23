from django.http import HttpResponse
from django.shortcuts import render

def HomeView(request):
    return render(request,'home.html')