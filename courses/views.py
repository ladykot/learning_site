# from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Teacher


def home_page(request, *args, **kwargs):
    # return HttpResponse('<h1> Hello world</h1>')
    template_name = "courses/home.html"
    title = 'Home'
    my_title = 'Lets study!'
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context = {'title': my_title}
    if request.user.is_authenticated:
        context = {'title': title, 'my_title': my_title,
                   'courses': courses, 'teachers': teachers}
        return render(request, template_name, context)


def course_detail_page(request):
    template_name = "courses/course_detail.html"
    title = 'Detail course'
    my_title = 'About this course:'
    one_course = Course.objects.first()  # выберем пока первый курс из БД
    context = {'title': title, 'one_course': one_course, 'my_title': my_title}
    return render(request, template_name, context)
