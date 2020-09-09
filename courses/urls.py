from django.urls import path

from .views import (
    ListCourse,
    CourseDetail,
    CourseCreate,
    CourseUpdate,
    CourseDelete
)

app_name = 'courses'

urlpatterns = [
    path('', ListCourse.as_view(), name='course_list'),
    path('create/', CourseCreate.as_view(), name='course_create'),
    path('<str:slug>/', CourseDetail.as_view(), name='course_detail'),
    path('<str:slug>/update/', CourseUpdate.as_view(), name='course_update'),
    path('<str:slug>/delete/', CourseDelete.as_view(), name='course_delete'),
]
