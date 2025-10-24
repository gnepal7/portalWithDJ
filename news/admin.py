from django.contrib import admin
from django.db import models
from mptt.admin import DraggableMPTTAdmin
from .models import News, Category, Author, Advertisement, Page, Logo
from cabinet.fields import CabinetForeignKey

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    list_per_page = 20

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'published_date', 'news_author')
    list_filter = ('published_date', 'categories')
    search_fields = ('news_title', 'news_subTitle', 'news_author__name')
    filter_horizontal = ('categories',)
    raw_id_fields = ['news_image', 'news_author']
    formfield_overrides = {
        models.ForeignKey: {'required': False},
        CabinetForeignKey: {'required': False},  
        models.CharField: {'required': False}
    }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    raw_id_fields = ['profile_image']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'link')
    list_filter = ('position',)
    search_fields = ('name',)
    raw_id_fields = ['image']
    formfield_overrides = {
        CabinetForeignKey: {'required': False},
        models.CharField: {'required': False},
        models.URLField: {'required': False},
    }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')
    raw_id_fields = ['image']
    formfield_overrides = {
        CabinetForeignKey: {'required': False},
    }

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    raw_id_fields = ['image']
    formfield_overrides = {
        CabinetForeignKey: {'required': False},
    }