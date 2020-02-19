from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')

def site02_dash(request):
    return render(request, 'pages/site02_dash.html')

def site03_dash(request):
    return render(request, 'pages/site03_dash.html')

def site04_dash(request):
    return render(request, 'pages/site04_dash.html')

def site05_dash(request):
    return render(request, 'pages/site05_dash.html')

def site06_dash(request):
    return render(request, 'pages/site06_dash.html')