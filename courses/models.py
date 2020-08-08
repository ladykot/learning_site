from django.conf import settings
from django.db import models
from django.db.models import ForeignKey

from django.utils import timezone


class Teacher(models.Model):
    ''' Модель автора курса (преподавателя)
    '''
    SEX_CHOICES = (('m', 'Мужс.'), ('f', 'Женс.'))
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    date_joined = models.DateTimeField("Дата регистрации",
                                       auto_now_add=True)
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.pk} {self.full_name}'


class Student(models.Model):
    ''' Модель студента
    '''
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    date_joined = models.DateTimeField("Дата регистрации",
                                       auto_now_add=True)
    course = ForeignKey(
        "Course", on_delete=models.DO_NOTHING, verbose_name=("Курс"))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.pk} {self.full_name}'


class Course(models.Model):
    # ''' Модель курса
    # '''
    title = models.CharField(
        max_length=200, unique=True)
    description = models.TextField()
    slug = models.SlugField(default='')
    # если препод удаляется, то и его курс
    teacher = ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    # ''' Модель занятия 
    # (один курс - много занятий)
    # '''
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}'

    def list_lessons(self):
        """ Вывод списка занятий на курсе
        в формате:
        Дата/время/Название_занятия/Преподаватель
        """
        