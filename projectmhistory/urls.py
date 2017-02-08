"""projectmhistory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from appmhistory.views import PatientViewSet
from rest_framework.routers import SimpleRouter
from appmhistory import views

admin.autodiscover()

#router = SimpleRouter()
#router.register(r'appmhistory',PatientViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^patients/', views.PatientList.as_view()),
    url(r'^patients//(?P<pk>[0-9]+)/$', views.PatientDetail.as_view()),
   # url(r'^', include(router.urls)),
   # url(r'^', include(router.urls)),
]
