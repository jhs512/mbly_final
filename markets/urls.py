from django.urls import path

from . import views

app_name = 'markets'

urlpatterns = [
    path('', views.index, name='list'),
]
