from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [

    path('',views.home,name='home'),
    path('api/v1/on-covid-19/check/',views.create_data,name='impact_default'),
    path('api/v1/on-covid-19/json/',views.create_data,name='impact_json'),
    path('api/v1/on-covid-19/xml/',views.create_data_xml,name='impact_xml'),
    path('api/v1/on-covid-19/logs/',views.log_request,name='impact_logs'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
