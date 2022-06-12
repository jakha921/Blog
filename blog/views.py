from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import Category, Men

# Create your views here.

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}]

def index(request):
    posts = Men.objects.all()
    cats  = Category.objects.all()
    context = {
        'menu' : menu,
        'title' : 'Main page',
        'posts' : posts,
        'category' : cats,
        'cat_selected' : 0,
    }
    return render(request, 'blog/index.html', context)   # third el is var key & value


# Error 404
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Sorry but i can find this page</h1>")

def about(request):
    return render(request, 'blog/about.html', {'menu' : menu, 'title' : 'About'}) # use render for rendering html template
    # return HttpResponse("About")
    
def addpage (request):
    return HttpResponse("Add post")

def contact(request):
    return HttpResponse ("Contact")

def login(request):
    return HttpResponse ("Login")

def show_post(request, post_id):
    return HttpResponse (f"Post id {post_id}")

def show_category(request, cat_id):
    posts = Men.objects.filter(category_id=cat_id)
    cats  = Category.objects.all()
    
    if len(posts) == 0:
        raise page_not_found()
    
    context = {
        'menu' : menu,
        'title' : 'Displays on the headings',
        'posts' : posts,
        'category' : cats,
        'cat_selected' : cat_id,
    }
    return render(request, 'blog/index.html', context)   # third el is var key & value
