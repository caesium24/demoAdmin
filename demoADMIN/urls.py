from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from splunkalerts import views

urlpatterns = [
    path('', include('pages.urls')),
    path('metrics/', include('metrics.urls')),
    path('alerts/', include('alerts.urls')),
    path('tickets/', include('tickets.urls')),
    path('admin/', admin.site.urls),
    url(r'^webhook', views.webhook, name='webhook'),

]
