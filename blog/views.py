from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def category(request, catId):
    return HttpResponse(f"<h1>You're looking at category. <b>{catId}</b></h1>")

# def category(request, cat):
#     if request.GET:
#         print(request.GET)
    # http://127.0.0.1:8000/cat/qwer/?name=Jakhongir&age=21
    # <QueryDict: {'name': ['Jakhongir'], 'age': ['21']}>
    # return HttpResponse(f"<h1>You're looking at category. <b>{cat}</b></h1>")


# Error 404
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Sorry but i can find this page</h1>")


# redirect by name
def archive(request, year):
    if int(year) > 2021:
        return redirect('home')
    return HttpResponse(f"<h1>You're looking at archieve. <b>{year}</b></h1>")