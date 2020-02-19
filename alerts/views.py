from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def site01_alerts(request):
    return render(request, 'alerts/site01_alerts.html')

def site02_alerts(request):
    return render(request, 'alerts/site02_alerts.html')

def site03_alerts(request):
    return render(request, 'alerts/site03_alerts.html')

def site04_alerts(request):
    return render(request, 'alerts/site04_alerts.html')

def site05_alerts(request):
    return render(request, 'alerts/site05_alerts.html')

def site06_alerts(request):
    return render(request, 'alerts/site06_alerts.html')