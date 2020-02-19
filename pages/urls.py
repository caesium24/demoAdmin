from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('site02_dash', views.site02_dash, name='site02_dash'),
    path('site03_dash', views.site03_dash, name='site03_dash'),
    path('site04_dash', views.site04_dash, name='site04_dash'),
    path('site05_dash', views.site05_dash, name='site05_dash'),
    path('site06_dash', views.site06_dash, name='site06_dash')

]
