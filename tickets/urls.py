from django.urls import path

from . import views

urlpatterns = [
    path('site01_tickets', views.site01_tickets, name='site01_tickets'),
    path('site02_tickets', views.site02_tickets, name='site02_tickets'),
    path('site03_tickets', views.site03_tickets, name='site03_tickets'),
    path('site04_tickets', views.site04_tickets, name='site04_tickets'),
    path('site05_tickets', views.site05_tickets, name='site05_tickets'),
    path('site06_tickets', views.site06_tickets, name='site06_tickets')

]