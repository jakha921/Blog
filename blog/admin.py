from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Men, Category

# Register your models here.
# admin.site.register(Men)  # First method of registration

@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo', 'time_create', 'is_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)
    prepopulated_fields = {'slug': ('title',)}      # генерация slug url ASCII
    fields = ('title', 'slug', 'content', 'photo', 'get_photo', 'time_create', 'time_update', 'is_published', 'category', )
    readonly_fields = ('time_create', 'time_update', 'get_photo')
    # radio_fields = {"category": admin.VERTICAL}   # radio btn
    save_on_top = True                            # btn save on top
    autocomplete_fields = ['category']              # search field FK 
    save_as = True
    search_help_text = 'Search title & content'     # show help text under search field
    view_on_site = True                            # link for this content if have  get_absolute_url()
    actions_selection_counter = True                # counter selected elements

    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60"')
            
    get_photo.short_description = 'img'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.site_header = 'Admin panel for a blog about Men'
admin.site.site_title = 'Blog admin panel'