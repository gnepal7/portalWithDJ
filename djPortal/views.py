from itertools import count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from mptt.templatetags.mptt_tags import get_cached_trees
from news.models import News, Category, Author, Page, Logo

def landingPage(request):
    flash_news = News.objects.filter(categories__name='flashNews').order_by('-id')[:2]
    feature_news = News.objects.filter(categories__name='featured').order_by('-id')[:2]
    taja_news = News.objects.exclude(categories__name__in=['flashNews', 'featured']).order_by('-id')[:6]
    main_news = News.objects.filter(categories__name='mainNews').order_by('-id')[:6]
    pol_news = News.objects.filter(categories__name='राजनीति').order_by('-id')[:5]
    edu_news = News.objects.filter(categories__name='शिक्षा').order_by('-id')[:4]
    health_news = News.objects.filter(categories__name='स्वास्थ्य').order_by('-id')[:6]
    economic_news = News.objects.filter(categories__name='अर्थ').order_by('-id')[:6]
    international_news = News.objects.filter(categories__name='अन्तर्राष्ट्रिय').order_by('-id')[:4]
    bichar_views = News.objects.filter(categories__name='विचार').order_by('-id')[:2]
    inter_views = News.objects.filter(categories__name='अन्तरवार्ता').order_by('-id')[:2]
    local_level = News.objects.filter(categories__name='स्थानीय तह').order_by('-id')[:3]
    photo_gal = News.objects.filter(categories__name='फोटोफिचर').order_by('-id')[:3]
    suchana_prabidhi = News.objects.filter(categories__name='सूचना-प्रविधि').order_by('-id')[:6]
    paryaton_news = News.objects.filter(categories__name='पर्यटन').order_by('-id')[:2]
    kala_sahitya = News.objects.filter(categories__name='संस्कृति-कला-साहित्य').order_by('-id')[:6]
    patra_patrika = News.objects.filter(categories__name='पत्रपत्रिका').order_by('-id')[:3]
    vivid = News.objects.filter(categories__name='vivid').order_by('-id')[:3]
    manoranjan = News.objects.filter(categories__name='मनोरञ्जन').order_by('-id')[:3]
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    logo = Logo.objects.first()
    newsData = {
        'flashnews': flash_news,
        'featured': feature_news,
        'tajanews': taja_news,
        'mainNews' : main_news,
        'rajnitiNews': pol_news,
        'eduNews' : edu_news,
        'healthNews': health_news,
        'ecoNews': economic_news,
        'intNews': international_news,
        'bicharViews': bichar_views,
        'interViews': inter_views,
        'localNews': local_level,
        'photoFeatures': photo_gal,
        'suchanaPrabidhi': suchana_prabidhi,
        'paryatonNews': paryaton_news,
        'kalaNews': kala_sahitya,
        'patrikaNews': patra_patrika,
        'vividNews' : vivid,
        'manorajnanNews' : manoranjan,
        'categories': categories,
        'title': 'News Portal',
        'logo': logo
    }
    return render(request, 'index.html', newsData)

def newsListing(request, category):
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    category = get_object_or_404(Category, name=category)
    news_list = News.objects.filter(categories=category).order_by('-published_date')[:1]  # Limit to 1 banner item
    paginated_news = News.objects.filter(categories=category).order_by('-published_date')
    paginator = Paginator(paginated_news, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    logo = Logo.objects.first()
    return render(request, 'listing.html', {
        'category': category,
        'news_list': news_list,
        'page_obj': page_obj,
        'categories': categories,
        'title': category.name,
        'logo': logo
    })

def newsDetail(request, id):
    news = get_object_or_404(News, id=id)
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    related_news = News.objects.filter(categories__in=news.categories.all()).exclude(id=news.id).order_by('-published_date')[1:7]
    popular_news = News.objects.all().order_by('-published_date')[:7] 
    logo = Logo.objects.first()
    return render(request, 'newsDetail.html', {
        'news': news,
        'categories': categories,
        'related_news': related_news,
        'popular_news': popular_news,
        'title': news.news_title,
        'logo': logo
    })

def authorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    logo = Logo.objects.first()
    return render(request, 'author.html', {
        'author': author, 
        'categories': categories, 
        'title': author.name or 'Author Profile',
        'logo': logo
        })


def pageDetail(request, page_title):
    categories = get_cached_trees(Category.objects.exclude(name__in=['flashNews', 'mainNews', 'featured', 'vivid']))
    page = get_object_or_404(Page, title=page_title)
    logo = Logo.objects.first()
    return render(request, 'page.html', {
        'page': page,
        'base_url': 'http://127.0.0.1:8000/', 
        'categories': categories,
        'title': page.title,
        'logo': logo
    })
