
# from django import forms
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import News, Category

# from cabinet.admin import FileAdmin

# admin.site.register_file_model(FileAdmin)

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    list_per_page = 20
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'published_date', 'news_authorName')
    list_filter = ('published_date', 'categories')
    search_fields = ('news_title', 'news_subTitle', 'news_authorName')
    filter_horizontal = ('categories',)
    raw_id_fields = ['news_image']
