from django.db import models
from django.urls import reverse

# Create your models here.


class Men(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    content = models.TextField('post text', blank=True)
    photo = models.ImageField('celebrity photo', upload_to='photos/%Y/%m/%d/')
    time_create = models.DateField('post created', auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField('publication', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Popular man'
        verbose_name_plural = 'Popular men'
        ordering = ['time_create', 'title',]


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


