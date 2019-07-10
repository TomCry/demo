from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class DemoView(View):

    def get(self, request):
        return HttpResponse('get page')

    def post(self, request):
        return HttpResponse(' post page')


def my_decorator(view_func):

    def wrapper(request, *args, **kwargs):
        print("装饰器被调用")
        print(request.path)
        return view_func(request, *args, **kwargs)

    return wrapper
