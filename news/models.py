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

class Advertisement(models.Model):
    POSITION_CHOICES = [
        ('header-right', 'Header Right'),
        ('under-menu', 'Under Menu'),
        ('under-banner', 'Under Banner'),
        ('featured-top-left', 'Featured Top Left'),
        ('featured-bottom-left', 'Featured bottom Left'),
        ('under-featured', 'Under Featured'),
        ('mainNews-right', 'Right to Main News'),
        ('under-mainNews', 'Under MainNews'),
        ('under-rajniti', 'Under Rajniti'),
        ('under-health', 'Under Health'),
        ('under-artha', 'Under Artha'),
        ('under-international', 'Under International'),
        ('under-interview', 'Under Interview'),
        ('under-photo-feature', 'Under Photo Feature'),
        ('under-suchana-prabidhi', 'Under Suchana Prabidhi'),
        ('under-kala', 'Under Kala'),
        ('under-vivid-right', 'Right to vivid'),
        ('under-vivid', 'Under Vivid'),
        ('under-manoranjan', 'Under Manoranjan'),
        ('detail-top', 'Top on Detail'),
        ('detail-bottom1', 'Bottom1 on Detail'),
        ('detail-bottom2', 'Bottom2 on Detail'),

    ]
    position = models.CharField(max_length=70, choices=POSITION_CHOICES)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='ad_images')
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name or f"Ad at {self.position}"


class Page(models.Model):
    PAGE_TYPES = [
        ('हाम्रो टिम', 'हाम्रो टिम'),
        ('हाम्रो बारेमा', 'हाम्रो बारेमा'),
        ('गोपनीय नीति', 'गोपनीय नीति'),
        ('सम्पर्क गर्नुहोस्', 'सम्पर्क गर्नुहोस्'),
    ]
    title = models.CharField(max_length=50, choices=PAGE_TYPES, unique=True)
    image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='page_images')
    content = HTMLField()

    def __str__(self):
        return self.title

class Logo(models.Model):
    title = models.CharField(max_length=100)
    image = CabinetForeignKey('cabinet.File', null=True, blank=True, on_delete=models.SET_NULL, related_name='logo_images')

    def __str__(self):
        return self.title