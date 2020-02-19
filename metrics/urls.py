from django.urls import path

from . import views

urlpatterns = [
    path('site01_metrics', views.site01_metrics, name='site01_metrics'),
    path('site02_metrics', views.site02_metrics, name='site02_metrics'),
    path('site03_metrics', views.site03_metrics, name='site03_metrics'),
    path('site04_metrics', views.site04_metrics, name='site04_metrics'),
    path('site05_metrics', views.site05_metrics, name='site05_metrics'),
    path('site06_metrics', views.site06_metrics, name='site06_metrics')

]
