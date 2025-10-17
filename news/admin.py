# from django.contrib import admin

# from news.models import News

# # Register your models here.
# class NewsAdmin(admin.ModelAdmin):
#   list_display=('news_title', 
#                 'news_subTitle',
#                 'news_authorName',
#                 'news_authorImg',
#                 'published_date',
#                 'news_image',
#                 'news_desc'
#                 )

# admin.site.register(News, NewsAdmin)
# # Register your models here.



from django.contrib import admin
from .models import News, Category

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the News model with custom admin configuration
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'published_date', 'news_authorName')
    list_filter = ('published_date', 'categories')
    search_fields = ('news_title', 'news_subTitle', 'news_authorName')
    filter_horizontal = ('categories',)  # Displays categories as a horizontal checkbox-like interface

    # Optional: If you want to prepopulate the slug field based on the title
    prepopulated_fields = {'news_title': ('news_title',)}
