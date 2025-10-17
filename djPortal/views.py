from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from news.models import News

# def landingPage(request):
#     newsData = News.objects.all().order_by('-id')

#     newsData = {
#         'newsData': newsData
#     }
#     return render(request, 'index.html', newsData)

def landingPage(request):
    flash_news = News.objects.filter(categories__name='flashNews').order_by('-id')[:2]
    economic_news = News.objects.filter(categories__name='economic').order_by('-id')

    newsData = {
        'flashnews': flash_news,
        'economicNews': economic_news,
    }
    return render(request, 'index.html', newsData)



def newsListing(request):
    return render(request, 'listing.html')

def newsDetail(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'newsDetail.html', {'news': news})
