from itertools import count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from mptt.templatetags.mptt_tags import get_cached_trees
from news.models import News, Category, Author

def landingPage(request):
    flash_news = News.objects.filter(categories__name='flashNews').order_by('-id')[:2]
    feature_news = News.objects.filter(categories__name='featured').order_by('-id')[:2]
    taja_news = News.objects.exclude(categories__name__in=['flashNews', 'featured']).order_by('-id')[:6]
    main_news = News.objects.filter(categories__name='mainNews').order_by('-id')[:6]
    pol_news = News.objects.filter(categories__name='राजनीति').order_by('-id')[:5]
    edu_news = News.objects.filter(categories__name='शिक्षा').order_by('-id')[:4]
    health_news = News.objects.filter(categories__name='स्वास्थ्य').order_by('-id')[:6]
    economic_news = News.objects.filter(categories__name='economic').order_by('-id')
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    newsData = {
        'flashnews': flash_news,
        'featured': feature_news,
        'tajanews': taja_news,
        'mainNews' : main_news,
        'rajnitiNews': pol_news,
        'eduNews' : edu_news,
        'healthNews': health_news,
        'economicNews': economic_news,
        'categories': categories
    }
    return render(request, 'index.html', newsData)

def newsListing(request, category):
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    category = get_object_or_404(Category, name=category)
    news_list = News.objects.filter(categories=category).order_by('-published_date')[:1]  # Limit to 1 banner item
    paginated_news = News.objects.filter(categories=category).order_by('-published_date')
    paginator = Paginator(paginated_news, 10)  # Adjust per-page limit as needed
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listing.html', {
        'category': category,
        'news_list': news_list,
        'page_obj': page_obj,
        'categories': categories,  # For menu
    })

def newsDetail(request, id):
    news = get_object_or_404(News, id=id)
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    related_news = News.objects.filter(categories__in=news.categories.all()).exclude(id=news.id).order_by('-published_date')[1:7]
    popular_news = News.objects.all().order_by('-published_date')[:7] 
    return render(request, 'newsDetail.html', {
        'news': news,
        'categories': categories,
        'related_news': related_news,
        'popular_news': popular_news
    })

def authorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    return render(request, 'author.html', {'author': author, 'categories': categories})

