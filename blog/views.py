from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required   # decorator for login req
from django.core.paginator import Paginator                 # for pagination on func

from .models import Category, Men
from .forms import AddPostForm, RegisterUserForm
from .utils import DataMixin, menu

# Create your views here.


class MenListView(DataMixin, ListView):
    model = Men                         # tell him from which model to get this all data
    template_name = 'blog/index.html'   # return render(request, 'blog/index.html', context)
    context_object_name = 'posts'       # posts = Men.objects.all()
    # extra_context = {'title' : 'Main page'} # it not recomended because here use just for static data
    # paginate_by = 3                    # paginate the list view
    
    def get_context_data(self, *, object_list=None, ** kwargs):
        context = super().get_context_data(** kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):             # do this if you need check or doing smth
        return Men.objects.filter(is_published=True)



# Error 404
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Sorry but i can find this page</h1>")

# @login_required(login_url='/admin/')    # func work login request
def about(request):
    contact_list = Men.objects.all()
    paginator = Paginator(contact_list, 2) # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/about.html', {'page_obj': page_obj, 'menu' : menu, 'title' : 'About'}) # use render for rendering html template
    # return HttpResponse("About")


class MenAddPostCreateView(LoginRequiredMixin, DataMixin, CreateView):  # class login request work like this
    form_class = AddPostForm
    template_name = "blog/addpage.html"
    success_url = reverse_lazy('home')  # The difference between reverse & reverse_lasy is only created, and the second already exists
    # login_url = '/admin/'       # not auth redirect to login url
    raise_exception = True          # not allow or Forbidden
    
    
    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        c_def = self.get_user_context(title="Add post")
        return dict(list(context.items())+list(c_def.items()))


def contact(request):
    return HttpResponse ("Contact")

def login(request):
    return HttpResponse ("Login")


class MenPostDetailView(DataMixin, DetailView):
    model = Men
    template_name = "blog/post.html"
    slug_url_kwarg = 'post_slug'    # if use in url own slug field
    context_object_name = 'post'    # used on html for get a data from model
    
    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        c_def = self.get_user_context(title="post")
        return dict(list(context.items())+list(c_def.items()))


class MenCategoryListView(DataMixin, ListView):
    model = Men
    template_name = "blog/index.html"
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Men.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)     # url by slug

    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        c_def = self.get_user_context(title='Category ' +str(context['posts'][0].category),
                                        cat_selected = context['posts'][0].category_id )
        return dict(list(context.items())+list(c_def.items()))


class RegisterUserCreateView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "blog/register.html"
    success_url = reverse_lazy('login')
    
    def get_context_data(self,*,object_list=None,** kwargs):
        context=super().get_context_data(** kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items())+list(c_def.items()))

