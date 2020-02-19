from django.shortcuts import render
from django.http import HttpResponse
from .models import ticket
from .models import admins

def site01_tickets(request):
    tickets = ticket.objects.all()

    context = {
    'tickets': tickets
    }
    return render(request, 'tickets/site01_tickets.html', context)

def site02_tickets(request):
    return render(request, 'tickets/site02_tickets.html')

def site03_tickets(request):
    return render(request, 'tickets/site03_tickets.html')

def site04_tickets(request):
    return render(request, 'tickets/site04_tickets.html')

def site05_tickets(request):
    return render(request, 'tickets/site05_tickets.html')

def site06_tickets(request):
    return render(request, 'tickets/site06_tickets.html')