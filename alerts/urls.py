from django.urls import path

from . import views

urlpatterns = [
    path('site01_alerts', views.site01_alerts, name='site01_alerts'),
    path('site02_alerts', views.site02_alerts, name='site02_alerts'),
    path('site03_alerts', views.site03_alerts, name='site03_alerts'),
    path('site04_alerts', views.site04_alerts, name='site04_alerts'),
    path('site05_alerts', views.site05_alerts, name='site05_alerts'),
    path('site06_alerts', views.site06_alerts, name='site06_alerts')

]