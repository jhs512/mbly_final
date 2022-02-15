from django.contrib import admin


# Register your models here.
from .models import Market


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass