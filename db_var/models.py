from datetime import datetime

from django.db import models


# Create your models here.
class DbVar(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)
    expire_date = models.DateTimeField('만료날짜', null=True)
    name = models.CharField('변수이름', max_length=50, unique=True)
    value = models.TextField('변수값')

    @classmethod
    def set(cls, name, value, expire_date=None):
        try:
            db_var = cls.objects.get(name=name)
            db_var.value = value
            db_var.expire_date = expire_date
            db_var.save()
        except:
            cls.objects.create(name=name, value=value, expire_date=expire_date)

    @classmethod
    def get(cls, name, default_value):
        try:
            db_var = cls.objects.get(name=name)

            if not db_var.expire_date or (db_var.expire_date and db_var.expire_date > datetime.datetime.now()):
                return db_var.value
        except:
            return default_value

    @classmethod
    def remove(cls, name):
        try:
            cls.objects.get(name=name).delete()
        except:
            pass
