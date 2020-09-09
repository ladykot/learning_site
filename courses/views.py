from django.http import HttpResponseRedirect
# представления здесь

from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course, Teacher, Lesson

from .forms import CourseModelForm, StudentModelForm


# def home_page(request, *args, **kwargs):
#     ''' Главная страница со списком актуальных курсов
#     для зарегистрированных пользователей
#     '''
#     template_name = "courses/course_list.html"
#     title = 'Home'
#     my_title = 'Lets study!'
#     courses = Course.objects.all()
#     teachers = Teacher.objects.all()
#     context = {'title': my_title}
#     if request.user.is_authenticated:
#         context = {'title': title, 'my_title': my_title,
#                    'courses': courses, 'teachers': teachers}
#         return render(request, template_name, context)


# def course_detail_page(request, slug):
#     ''' Отображение одного курса
#     '''
#     template_name = "courses/detail.html"
#     one_course = get_object_or_404(Course, slug=slug)
#     student_form = StudentModelForm(request.POST or None)
#     list_lessons = Lesson.objects.filter(
#         course__title=one_course.title)  # список занятий на курсе

#     if student_form.is_valid():
#         student_form.save()
#         student_form = StudentModelForm()  # чистая форма

#     context = {
#         'one_course': one_course,
#         'student_form': student_form,
#         'list_lessons': list_lessons,
#     }
#     return render(request, template_name, context)


# class CourseDetail(TemplateView):
#     template_name = "courses/detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         one_course = get_object_or_404(Course, slug=self.kwargs.get('slug'))

#         list_lessons = Lesson.objects.filter(
#             course__title=one_course.title)  # список занятий на курсе
#         context.update({
#             'one_course': one_course,
#             'list_lessons': list_lessons
#         })

#         return context

class CourseDetail(DetailView):
    ''' Отображение одного курса
    '''
    model = Course
    context_object_name = 'one_course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        one_course = get_object_or_404(Course, slug=self.kwargs.get('slug'))

        list_lessons = Lesson.objects.filter(
            course__title=one_course.title)  # список занятий на курсе
        context.update({
            'one_course': one_course,
            'list_lessons': list_lessons
        })

        return context


# def course_list_view(request):
    #     ''' Страница со списком курсов
    #     '''
    #     course_list = Course.objects.all()
    #     template_name = "courses/list.html"
    #     context = {'course_list': course_list}
    #     return render(request, template_name, context)


class ListCourse(ListView):
    ''' Отображение списка курсов
    (с переходом на страницу курса)
    '''
    model = Course

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)  


# def course_create_view(request):
#     ''' Cтраница создания курса
#     '''
#     template_name = "courses/create.html"
#     title = 'Fill the form, please:'
#     course_form = CourseModelForm(request.POST or None)
#     if course_form.is_valid():
#         course_form.save()
#         course_form = CourseModelForm()  # чистая форма

#     context = {
#         'title': title,
#         'course_form': course_form
#     }
#     return render(request, template_name, context)

class CourseCreate(CreateView):
    ''' Cтраница создания курса
    '''
    model = Course
    success_url = reverse_lazy('courses:course_list')
    fields = '__all__'


class CourseUpdate(UpdateView):
    ''' Cтраница редактирования курса
    '''
    model = Course
    success_url = reverse_lazy('courses:course_list')
    fields = '__all__'


class CourseDelete(DeleteView):
    ''' Cтраница удаления курса
    '''
    model = Course
    success_url = reverse_lazy('courses:course_list')

    def delete(self, request, *args, **kwargs):  # перепишем метод delete
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# def course_delete_view(request):
#     ''' Cтраница удаления курса
#     '''
#     template_name = "courses/delete.html"
#     one_course = get_object_or_404(Course, slug=slug)
#     context = {'one_course': one_course}
#     return render(request, template_name, context)
