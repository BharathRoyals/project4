from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def xyz(request):
    return HttpResponse('sam is a good boy')