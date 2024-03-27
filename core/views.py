# from django.contrib import
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello, world.")