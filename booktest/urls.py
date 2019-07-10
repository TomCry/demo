__author__ = 'enzyme'
__date__ = '2019/7/10 1:57 PM'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^booktest/$', views.IndexView.as_view()),
]