from django.contrib import admin

from .models import Teacher, Course, Student, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'sex', 'first_name', 'last_name', 'date_joined'
    list_display_links = 'id',

# admin.site.register(Teacher, TeacherAdmin)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    def description_short(self, obj: Course):
        if len(obj.description) <= 30:
            return obj.description
        return f'{obj.description[:30]}...'
        
    list_display = 'id', 'title', 'description_short', 'teacher'    
    list_display_links = 'id', 'teacher', 'title'

    def __str__(self):
        return f'{self.id} {self.title}'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'date_joined'
    list_display_links = 'id',

    def __str__(self):
        return f'{self.id} {self.last_name}'

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'title', 'date', 'teacher'