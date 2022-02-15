from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['body']
        widgets = {
            'body': SummernoteWidget(),
        }
