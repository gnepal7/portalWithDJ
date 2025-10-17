# from django.db import models

# from tinymce.models import HTMLField

# # Create your models here.

# class News(models.Model):
#   news_title = models.CharField(max_length=100)
#   news_subTitle = models.CharField(max_length=100)
#   news_authorName = models.CharField(max_length=70)
#   news_authorImg = models.FileField(upload_to='news/', max_length=250, null=True, default=None, blank=True)
#   news_desc = HTMLField()
#   news_image = models.FileField(upload_to='news/', max_length=250, null=True, default=None, blank=True)
#   published_date = models.DateTimeField(auto_now_add=True)


from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Category name like 'Politics', 'Economics', etc.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_subTitle = models.CharField(max_length=100, null=True)
    news_authorName = models.CharField(max_length=70)
    news_authorImg = models.FileField(upload_to='news/', max_length=250, null=True, default=None, blank=True)
    news_desc = HTMLField()
    news_image = models.FileField(upload_to='news/', max_length=250, null=True, default=None, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='news')  # Many-to-many relationship with Category

    def __str__(self):
        return self.news_title
