from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def suni(request):
    return HttpResponse('she is very good girl')

def chintu(request):
    return HttpResponse('<h1>he is very innocent who is younger brother of lahari</h1>')
def a(request):
    return HttpResponse('''
    <''')