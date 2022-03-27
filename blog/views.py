from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def category(request):
    return HttpResponse("<h1>You're looking at category.</h1>")