from django import forms

from .models import Course, Student

class CourseModelForm(forms.ModelForm):
    ''' Форма для добавления нового курса
    '''
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'description']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        q = Course.objects.filter(title='title')
        print(title)
        if q.exists():
            raise forms.ValidationError('This title has already been used')
            
        return title
        

class StudentModelForm(forms.ModelForm):
    ''' Форма записи на курс
    '''
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']