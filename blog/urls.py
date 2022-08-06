from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    # path('', cache_page(60)(views.MenListView.as_view()), name='home'), 
    path('', views.MenListView.as_view(), name='home'), 
    path('about/', views.about, name='about'), 
    path('addpage/', views.MenAddPostCreateView.as_view(), name='add_page'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUserCreateView.as_view(), name='register'),
    path('post/<slug:post_slug>/', views.MenPostDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.MenCategoryListView.as_view(), name='category'),
]

