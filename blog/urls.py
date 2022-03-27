from django.urls import path, include
from . import views


urlpatterns = [
    # path('blog/', views.index), # http://127.0.0.1:8000/blog/
    path('blog/', views.index, name='home'), # http://127.0.0.1:8000/blog/
    
    path('cat/<int:catId>/', views.category), # http://127.0.0.1:8000/cat/1/
    # path('cat/<slug:cat>/', views.category), # http://127.0.0.1:8000/cat/star/    NOT RUSSIAN str
    
    path('archive/<int:year>/', views.archive),
]

