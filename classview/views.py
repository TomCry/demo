from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator


# Create your views here.


def my_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        print("装饰器被调用")
        print(request.path)
        return view_func(request, *args, **kwargs)

    return wrapper


# class DemoView(View):
#
#     @method_decorator(my_decorator)
#     def dispatch(self, request, *args, **kwargs):
#         super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         return HttpResponse('get page')
#
#     def post(self, request):
#         return HttpResponse(' post page')


@method_decorator(my_decorator, name='get')
class DemoView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('get page')

    def post(self, request):
        return HttpResponse(' post page')
