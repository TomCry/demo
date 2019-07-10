from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("hello, world")


def say(request):
    url = reverse('users:index')
    print(url)
    return HttpResponse("say")


