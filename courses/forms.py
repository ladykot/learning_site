from django import forms


class CourseForm(forms.Form):
    title = forms.CharField()
    fullname = forms.CharField()
    slug = forms.SlugField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    