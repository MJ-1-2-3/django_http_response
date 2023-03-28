from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is my second try and I won"t give up unitl I get this</h1>' )

# Create your views here.
