from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django_summernote.models import Attachment


class RelatedAttachment(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name = '서머노트 첨부파일'
        verbose_name_plural = '서머노트 첨부파일들'

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField('관련 데이터 번호')
    attachment = models.OneToOneField(Attachment, on_delete=models.DO_NOTHING)

    @property
    def url(self):
        return self.attachment.file.url
