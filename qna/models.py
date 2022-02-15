import re

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.utils.html import strip_tags
from django_summernote.models import Attachment

from accounts.models import User
from summernote_support.models import RelatedAttachment


class Question(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = '질문'
        verbose_name_plural = '질문들'

    def __str__(self):
        return f"{self.id}, {strip_tags(self.body)[:75] + (strip_tags(self.body)[75:] and '..')}"

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField('관련 데이터 번호')
    content_object = GenericForeignKey('content_type', 'object_id')
    body = models.TextField('내용')
    is_complete = models.BooleanField('답변완료여부', default=False)

    related_attachments = GenericRelation(RelatedAttachment)

    def extract_attachments(self) -> list[RelatedAttachment, ...]:
        img_urls = re.findall(r'src="(.*?)"', self.body)
        img_urls = [img_url.replace(settings.MEDIA_URL, '') for img_url in img_urls]

        return Attachment.objects.filter(file__in=img_urls)


class Answer(models.Model):
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.id}, {self.body[:75] + (self.body[75:] and '..')}"

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('내용')
