import re

from django.db import models

# Create your models here.
from django.db.models import Avg

from accounts.models import User
from tags.models import Tag


class Market(models.Model):
    class Meta:
        ordering = ('-id',)
        verbose_name = '마켓'
        verbose_name_plural = '마켓들'

    def __str__(self):
        return f"{self.id}, {self.name}"

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    name = models.CharField('마켓이름', max_length=100)
    site_url = models.URLField('마켓사이트URL', max_length=100)
    email = models.EmailField('마켓대표이메일', max_length=100)
    master = models.OneToOneField(User, on_delete=models.CASCADE)
    review_point = models.FloatField('리뷰평점', default=0)
    description = models.TextField('설명')
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        old_tags = self.tags.all()
        new_tags = self.extract_tag_list()

        delete_tags:list[Tag] = []
        add_tags:list[Tag] = []

        for old_tag in old_tags:
            if not old_tag in new_tags:
                delete_tags.append(old_tag)

        for new_tag in new_tags:
            if not new_tag in old_tags:
                add_tags.append(new_tag)

        for delete_tag in delete_tags:
            self.tags.remove(delete_tag)

        for add_tag in add_tags:
            self.tags.add(add_tag)

    def extract_tag_list(self) -> list[Tag, ...]:
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.description)
        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list
