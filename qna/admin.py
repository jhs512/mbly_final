from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from .models import Question


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

