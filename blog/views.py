from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Category, Men
from .forms import AddPostForm

# Create your views here.

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}]

class MenListView(ListView):
    model = Men                         # tell him from which model to get this all data
    template_name = 'blog/index.html'   # return render(request, 'blog/index.html', context)
    context_object_name = 'posts'       # posts = Men.objects.all()
    # extra_context = {'title' : 'Main page'} # it not recomended because here use just for static data
    
    def get_context_data(self, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self):             # do this if you need check or doing smth
        return Men.objects.filter(is_published=True)



# Error 404
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Sorry but i can find this page</h1>")

def about(request):
    return render(request, 'blog/about.html', {'menu' : menu, 'title' : 'About'}) # use render for rendering html template
    # return HttpResponse("About")


class MenAddPostCreateView(CreateView):
    form_class = AddPostForm
    template_name = "blog/addpage.html"
    success_url = reverse_lazy('home')  # The difference between reverse & reverse_lasy is only created, and the second already exists
    
    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        context['title']='Add post'
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse ("Contact")

def login(request):
    return HttpResponse ("Login")


class MenPostDetailView(DetailView):
    model = Men
    template_name = "blog/post.html"
    slug_url_kwarg = 'post_slug'    # if use in url own slug field
    context_object_name = 'post'    # used on html for get a data from model
    
    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        context['title']=context['post']
        context['menu']=menu
        return context


class MenCategoryListView(ListView):
    model = Men
    template_name = "blog/index.html"
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Men.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)     # url by slug

    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        print(context)
        context['title']='Category ' +str(context['posts'][0].category)
        context['menu']=menu
        context['cat_selected']=context['posts'][0].category_id
        return context
