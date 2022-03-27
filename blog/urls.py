from django.urls import path, include
from . import views


urlpatterns = [
    path('blog/', views.index), # http://127.0.0.1:8000/blog/
    path('category/', views.category), # http://127.0.0.1:8000/category/
]
