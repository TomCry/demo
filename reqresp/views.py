from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def weather(request, city, year):
    print(city)
    print(year)
    return HttpResponse("ok")


def demo_response(request):
    request.session['user_id'] = 100
    request.session['username'] = 'python'

    return JsonResponse({'city': 'beijing', 'subject': 'python'})
