from django.db import models
from tinymce.models import HTMLField
from mptt.models import MPTTModel, TreeForeignKey
from cabinet.fields import CabinetForeignKey
from django.templatetags.static import static

class Category(MPTTModel):
    name = models.CharField(max_length=50)    
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.PositiveIntegerField(default=0)
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

class Author(models.Model):
    name = models.CharField(max_length=70)
    profile_image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='author_profiles')
    short_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def get_author_display(self):
        image = self.profile_image.file.url if self.profile_image else static('images/man.jpg')
        name = self.name if self.name else 'पोर्टल रिपोर्टर'
        return {'image': image, 'name': name}

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_subTitle = models.CharField(max_length=100, null=True, blank=True)
    news_author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='news')
    news_desc = HTMLField()
    news_image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='news_images')
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='news')

    def __str__(self):
        return self.news_title
