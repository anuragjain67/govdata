from django.conf.urls import patterns, include, url
from django.contrib import admin

from pincodeapp.api import PincodeResource
from pincodeapp import views

admin.autodiscover()

pincode_resource = PincodeResource()

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(pincode_resource.urls)),
)
