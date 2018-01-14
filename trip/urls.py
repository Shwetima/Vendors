from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Job_allotment/$', views.joballot, name='joballot'),
    url(r'^Tolltag/$', views.tolltag, name='tolltag'),
    url(r'^Tripsheet/$', views.tripsheet, name='tripsheet'),
    url(r'^Triplog/$', views.Ttriplog, name='Ttriplog'),
    url(r'^Drivertrace/$', views.Drivertrace, name='Drivertrace'),
    url(r'^Triplogtrace/$', views.Triplogtrace, name='Triplogtrace'),
    url(r'^Tripexpense/$', views.Tripexpense, name='Tripexpense'),
    url(r'^Vehicleauth/$', views.Vehicleauth, name='Vehicleauth'),



    url(r'^trip_advance/$', views.trip_advance, name='trip_advance'),
    url(r'^trip_log/$', views.triplog, name='triplog'),
    url(r'^tolllog/$', views.tolllog, name='tolllog'),
    url(r'^TripEntry/$', views.TripEntry, name='TripEntry'),
    url(r'^tollverification/$', views.tollverification, name='tollverification'),





    ]