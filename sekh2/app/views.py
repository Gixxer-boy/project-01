from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def eren(request):
    return HttpResponse ('<h1><marquee>sekhar</h1></marquee>')