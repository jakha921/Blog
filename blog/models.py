from django.db import models

# Create your models here.


class Men(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


