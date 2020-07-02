from django.conf import settings
from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


class Teacher(models.Model):
    ''' Модель автора курса (преподавателя)
    '''
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.id} {self.full_name}'


class Course(models.Model):
    ''' Модель курса
    '''
    title = models.CharField(
        max_length=200, unique=True)  # уникальное название курса
    description = models.TextField()  # описание курса
    # у каждого курса есть автор (преподаватель)
    teacher = ForeignKey(Teacher, on_delete=models.CASCADE,
                         default='Автор курса') 

    def __str__(self):
        return self.title


class Student(models.Model):
    pass

