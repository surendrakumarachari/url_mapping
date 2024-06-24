from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(reqest):
    return HttpResponse('<h1>srujana thinnava ra</h1>')

def login(request):
    return HttpResponse('<h1>this is login page</h1>')