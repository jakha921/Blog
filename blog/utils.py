from django.db.models import Count
from django.core.cache import cache
from .models import Category

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        ]

class DataMixin:
    paginate_by = 3
    
    def get_user_context(self,** kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats =  Category.objects.annotate(Count('men'))   # if len posts < 0 not show this cat
            cache.set('cats', cats, 60)                         # if not cached this cache and add to cache
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        
        context['menu']=user_menu
        context['cats']=cats
        if'cat_selected'not in context:
            context['cat_selected']=0
        return context