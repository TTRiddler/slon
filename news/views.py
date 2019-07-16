from django.shortcuts import render, get_object_or_404
from django.views import View
from news.models import News
from landing.pagination import pagination


class NewsView(View):
    def get(self, request):
        news = News.objects.filter(is_active=True)

        page_number = request.GET.get('page', 1)
        is_paginated, page, next_url, prev_url = pagination(news, page_number, 10)
        
        context = {
            'is_paginated': is_paginated,
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        return render(request, 'news/news.html', context)


class NewsDetailView(View):
    def get(self, request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)
        
        context = {
            'news_item': news_item,
        }

        return render(request, 'news/news_detail.html', context)