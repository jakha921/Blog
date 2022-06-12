from django.contrib import admin
from .models import Men

# Register your models here.
# admin.site.register(Men)  # First method of registration

@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    
