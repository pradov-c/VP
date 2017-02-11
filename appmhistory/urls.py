from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from appmhistory import views

urlpatterns = [
    url(r'^appmhistory/$', views.patient_list),
    url(r'^appmhistory/(?P<pk>[0-9]+)/$', views.patient_detail),
]