import logging

from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    logger = logging.getLogger('app')  # 위에서 등록해 놓은 app 로거 사용
    logger.info("INFO 레벨로 출력")  # 테스트

    return render(request, "home/main.html")
