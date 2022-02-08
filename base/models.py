from django.db import models

# https://velog.io/@kim6515516/장고에서-모델-소프트-삭제-구현하기
from django.utils.timezone import now


class SoftDeleteManager(models.Manager):
    use_for_related_fields = True  # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

    def get_queryset(self):
        return super().get_queryset().filter(delete_date__isnull=True)


class SoftDeleteModel(models.Model):
    delete_date = models.DateTimeField('삭제날짜', blank=True, null=True, default=None)

    class Meta:
        abstract = True  # 상속 할수 있게

    objects = SoftDeleteManager()  # 커스텀 매니저

    def delete(self, using=None, keep_parents=False):
        self.delete_date = now()
        self.save(update_fields=['delete_date'])

    def restore(self):  # 삭제된 레코드를 복구한다.
        self.delete_date = None
        self.save(update_fields=['delete_date'])
