from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [

    path('check/',views.create_data,name='impact_default'),
    path('json/',views.create_data,name='impact_json'),
    path('xml/',views.create_data_xml,name='impact_xml'),
#    path('logs/',views.log_request(),name='impact_logs'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
