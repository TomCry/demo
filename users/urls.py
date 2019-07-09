__author__ = 'enzyme'
__date__ = '2019/7/9 2:54 PM'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
]