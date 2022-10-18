from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("this is my 1st project")
def morning(request):
    return HttpResponse("im feeling good")
def good(request):
    return HttpResponse("moring's is cool cool")
def end(request):
    return HttpResponse("the end")
