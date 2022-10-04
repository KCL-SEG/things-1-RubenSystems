from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<html><head><title>Things</title></head><body><h1>Things</h1></body></html>")