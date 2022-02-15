from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from markets.models import Market


def index(request: HttpRequest):
    page = request.GET.get('page', '1')
    search_hash_tag_keyword = request.GET.get('search_hash_tag_keyword', '')
    search_hash_tag_keywords = search_hash_tag_keyword and search_hash_tag_keyword.split(' ')

    markets = Market.objects.order_by('-id').distinct()

    if search_hash_tag_keywords:
        markets = markets\
            .filter(tags__name__in=search_hash_tag_keywords)

    paginator = Paginator(markets, 4)  # 페이지당 10개씩 보여주기
    markets = paginator.get_page(page)

    return render(request, "markets/index.html", {
        "markets": markets
    })
