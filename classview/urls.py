__author__ = 'enzyme'
__date__ = '2019/7/10 9:02 AM'

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^demoview/$', views.my_decorator(views.DemoView.as_view())),
    url(r'^demoview/$', views.DemoView.as_view()),
]