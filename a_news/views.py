from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.


def home(request):
    categories = ['capital', 'nation', 'politics', 'global',
                  'stock', 'sports', 'science_tech', 'weather']
    news_by_category = {category: News.objects.filter(
        category=category) for category in categories}

    return render(request, 'a_news/home.html', {'news_by_category': news_by_category})


def news(request, pk):
    # news_category = get_object_or_404(News, pk=pk)
    all_news = News.objects.all()
    news = News.objects.get(pk=pk)
    context = {
        'news': news,
        # 'news_category': news_category,
        'all_news': all_news
    }
    return render(request, 'a_news/news.html', context)


def login(reqest):
    return render(reqest, 'form.html')
