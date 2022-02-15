from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from markets.models import Market
from tags.models import Tag


def index(request: HttpRequest):
    page = request.GET.get('search_keyword', '1')
    search_keyword = request.GET.get('search_keyword', '')
    search_keywords = search_keyword.split(' ')

    markets = Market.objects.order_by('-id').distinct()

    if search_keywords:
        markets = markets\
            .filter(tag_set__name__in=search_keywords)

    paginator = Paginator(markets, 4)  # 페이지당 10개씩 보여주기
    markets = paginator.get_page(page)

    return render(request, "markets/index.html", {
        "markets": markets
    })
