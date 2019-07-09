__author__ = 'enzyme'
__date__ = '2019/7/9 3:47 PM'

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
]