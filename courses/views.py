# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher

from .forms import CourseForm


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
    # title = 'Detail course'
    one_course = get_object_or_404(Course, slug=slug)
    context = {'one_course': one_course}
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
    print(request.POST)
    template_name = "courses/create.html"
    form = CourseForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        
    context = {
        'title': 'Fill the form, please:',
        'form': form
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
