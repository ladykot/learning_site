from django.urls import path, re_path, include
from django.contrib import admin

from .views import (
    home_page,
    course_detail_page,
    course_create_view,
    course_update_view,
    course_delete_view,
    course_list_view
)

app_name = 'courses'

urlpatterns = [
    # path('', home_page, name='home'),
    path('', course_list_view),
    path('<str:slug>/', course_detail_page),
    path('<str:slug>/update/', course_update_view, name='course_update'),
    path('<str:slug>/delete/', course_delete_view, name='course_delete'),
]
