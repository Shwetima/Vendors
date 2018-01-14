
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^Jobsheet/$', views.jobsheet, name='jobsheet'),
    url(r'^MRN_Invoice/$', views.mrninvoice, name='mrninvoice'),
    url(r'^Tyre_Inward/$', views.tyreinward, name='tyreinward'),
    url(r'^Tyre_Issue_to_Vehicle/$', views.tyreissue, name='tyreissue'),
    url(r'^Tyre_status/$', views.tyrestatus, name='tyrestatus'),
    url(r'^Tyre_brand_master/$', views.tyrebrand, name='tyrebrand'), 
    url(r'^Tyre_outward/$', views.tyreoutward, name='tyreoutward'),
    url(r'^Tyre_str_transfer/$', views.Tyrestrtransfer, name='Tyrestrtransfer'),
    url(r'^Tyre_Vendor_Bill/$', views.Tyrevendor, name='Tyrevendor'),
    url(r'^Update_Tyre/$', views.Updatetyre, name='Updatetyre'),
    url(r'^Tyre_Reciept_from_Vehicle/$', views.tyrereciept, name='tyrereciept'),
    url(r'^Tyre_trace/$', views.tyretrace, name='tyretrace'),
    url(r'^Tyre_without_reciept/$', views.tyrwithoutreciept, name='tyrwithoutreciept'),
    url(r'^Tyre_without_issue/$', views.tyrwithoutissue, name='tyrwithoutissue'),
    
    url(r'^tyre/$', views.recindex, name='recindex'),
    url(r'^rec/add$', views.recadd, name='recadd'),
    url(r'^rec/create$', views.reccreate, name='reccreate'),
    url(r'^tyre/edit/(?P<id>\d+)$', views.recedit, name='recedit'),
    url(r'^rec/edit/update/(?P<id>\d+)$', views.recupdate, name='recupdate'),
    url(r'^tyre/delete/(?P<id>\d+)$', views.recdelete, name='recdelete'),
]
