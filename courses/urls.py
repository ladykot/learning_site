from django.urls import path, re_path, include
from django.contrib import admin

from .views import (
    home_page,
    course_detail_page
)

app_name = 'courses'

urlpatterns = [
    path('', home_page, name='home'),
    path('course/', course_detail_page, name='course_detail')
]

