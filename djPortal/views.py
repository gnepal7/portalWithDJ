from itertools import count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from mptt.templatetags.mptt_tags import get_cached_trees
from news.models import News, Category

def landingPage(request):
    flash_news = News.objects.filter(categories__name='flashNews').order_by('-id')[:2]
    main_news = News.objects.filter(categories__name='mainNews').order_by('-id')[:2]
    taja_news = News.objects.exclude(categories__name__in=['flashNews', 'mainNews']).order_by('-id')[:6]
    # taja_news = News.objects.annotate(
    #     other_cat_count=count('categories', filter=Q(categories__name__in=['flashNews', 'mainNews'], distinct=True)) # type: ignore
    # ).filter(other_cat_count=0).order_by('-id')[:6]
    economic_news = News.objects.filter(categories__name='economic').order_by('-id')
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews']))
    # categories = Category.objects.all(Category.objects.exclude(name__in=['flashNews']))
    # categories = Category.objects.all()
    newsData = {
        'flashnews': flash_news,
        'mainNews' : main_news,
        'tajanews' : taja_news,
        'economicNews': economic_news,
        'categories': categories
    }
    return render(request, 'index.html', newsData)

def newsListing(request, category):
    category_obj = get_object_or_404(Category, name=category)
    news_list = News.objects.filter(categories=category_obj).order_by('-id')
    paginator = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'main-news']))

    context = {
        'category': category_obj,
        'page_obj': page_obj,
        'news_list': page_obj.object_list,
        'categories': categories,
    }
    return render(request, 'listing.html', context)

def newsDetail(request, id):
    news = get_object_or_404(News, id=id)
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'main-news']))
    
    return render(request, 'newsDetail.html', {
        'news': news,
        'categories': categories,
    })