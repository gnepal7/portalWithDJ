from django.db import models
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey

from cabinet.fields import CabinetForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=50)    
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.PositiveIntegerField(default=0)
    # Explicitly define MPTT fields with defaults
    level = models.PositiveIntegerField(default=0)
    lft = models.PositiveIntegerField(default=1)
    rght = models.PositiveIntegerField(default=1)
    tree_id = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['order']
        

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_subTitle = models.CharField(max_length=100, null=True)
    news_authorName = models.CharField(max_length=70)
    # news_authorImg = models.FileField(upload_to='news/', max_length=250, null=True, blank=True) 
    
    news_authorImg = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='author_images')

    news_desc = HTMLField()
    # news_image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL) 
    news_image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='news_images')
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='news')

    def __str__(self):
        return self.news_title

