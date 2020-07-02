from django.urls import path, include
from django.contrib import admin

from .views import index_view


app_name = 'courses'

urlpatterns = [
    path('', index_view, name='index'),
]