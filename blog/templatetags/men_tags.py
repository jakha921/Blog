from django import template
from blog.models import *

register = template.Library()


# @register.simple_tag()    # простой тег который вызывается как  get_category_list в шаблоне
@register.simple_tag(name='category')   # тег который вызывается как  category в шаблоне
def get_category_list(filter = None):
    if filter is None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('blog/category_list.html')
def show_category(sort=None, cat_selected=0):
    if sort is None:
        cats =  Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}