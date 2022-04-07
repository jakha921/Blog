from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'), # http://127.0.0.1:8000/blog/
    path('about/', views.about, name='about'), # http://127.0.0.1:8000/about/
]

