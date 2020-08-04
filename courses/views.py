# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher

from .forms import CourseModelForm, StudentModelForm


def home_page(request, *args, **kwargs):
    ''' Главная страница со списком актуальных курсов
    '''
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


def course_detail_page(request, slug):
    ''' Страница просмотра одного курса
    '''
    template_name = "courses/detail.html"
    title = 'Do you want to catch the course?'
    one_course = get_object_or_404(Course, slug=slug)
    student_form = StudentModelForm(request.POST or None)
    if student_form.is_valid():
        student_form.save()
        student_form = StudentModelForm()  # чистая форма
    
    context = {
        'title': title,
        'one_course': one_course,
        'student_form': student_form
    }
    return render(request, template_name, context)


def course_list_view(request):
    ''' Страница со списком курсов 
    '''
    course_list = Course.objects.all()
    template_name = "courses/list.html"
    context = {'course_list': course_list}
    return render(request, template_name, context)


def course_create_view(request):
    ''' Cтраница создания курса
    '''
    template_name = "courses/create.html"
    title = 'Fill the form, please:'
    course_form = CourseModelForm(request.POST or None)
    if course_form.is_valid():
        course_form.save()
        course_form = CourseModelForm()  # чистая форма
    
    context = {
        'title': title,
        'course_form': course_form
    }
    return render(request, template_name, context)


def course_update_view(request):
    ''' Cтраница редактирования курса   
    '''
    template_name = "courses/update.html"
    one_course = get_object_or_404(Course, slug=slug)
    context = {'one_course': one_course, 'form': None}
    return render(request, template_name, context)


def course_delete_view(request):
    ''' Cтраница удаления курса
    '''
    template_name = "courses/delete.html"
    one_course = get_object_or_404(Course, slug=slug)
    context = {'one_course': one_course}
    return render(request, template_name, context)
