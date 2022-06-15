from gc import get_objects
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Category, Men
from .forms import AddPostForm

# Create your views here.

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}]

def index(request):
    posts = Men.objects.all()
    context = {
        'menu' : menu,
        'title' : 'Main page',
        'posts' : posts,
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
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Men.objects.create(**form.cleaned_data)
                return redirect('home')
            except :
                form.add_error(None, "Error during adding the post")
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu' : menu, 'title' : 'Add page'})

def contact(request):
    return HttpResponse ("Contact")

def login(request):
    return HttpResponse ("Login")

def show_post(request, post_slug):
    post = get_object_or_404(Men, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.category_id
    }

    return render(request, 'blog/post.html', context)

def show_category(request, cat_id):
    posts = Men.objects.filter(pk=cat_id)
    
    if len(posts) == 0:
        raise page_not_found()
    
    context = {
        'menu' : menu,
        'title' : 'Displays on the headings',
        'posts' : posts,
        'cat_selected' : cat_id,
    }
    return render(request, 'blog/index.html', context)   # third el is var key & value
