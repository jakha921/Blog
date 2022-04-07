from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import Men

# Create your views here.

menu = ['Home', 'About', 'Add post', 'Feedback', 'Login']

def index(request):
    # return HttpResponse("Hello, world. You're at the blog index.")
    posts = Men.objects.all()
    return render(request, 'blog/index.html', {'menu' : menu, 'title' : 'Main page', 'posts' : posts})   # third el is var key & value

def about(request):
    return render(request, 'blog/about.html', {'menu' : menu, 'title' : 'About'}) # use render for rendering html template


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