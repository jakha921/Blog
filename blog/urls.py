from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MenListView.as_view(), name='home'), # http://127.0.0.1:8000/blog/
    path('about/', views.about, name='about'), # http://127.0.0.1:8000/about/
    path('addpage/', views.MenAddPostCreateView.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.RegisterUserCreateView.as_view(), name='register'),
    path('post/<slug:post_slug>/', views.MenPostDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.MenCategoryListView.as_view(), name='category'),
]

