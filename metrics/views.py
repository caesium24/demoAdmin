from django.shortcuts import render
from django.http import HttpResponse


def site01_metrics(request):
    return render(request, 'metrics/site01_metrics.html')

def site02_metrics(request):
    return render(request, 'metrics/site02_metrics.html')

def site03_metrics(request):
    return render(request, 'metrics/site03_metrics.html')

def site04_metrics(request):
    return render(request, 'metrics/site04_metrics.html')

def site05_metrics(request):
    return render(request, 'metrics/site05_metrics.html')

def site06_metrics(request):
    return render(request, 'metrics/site06_metrics.html')