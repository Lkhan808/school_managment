from django import forms
from students.models import Student, Grade


class StudentCreateForm(forms.ModelForm):
    grade = forms.ModelChoiceField(queryset=Grade.objects.all())

    class Meta:
        model = Student
        fields = ['photo', 'full_name', 'email', 'birth_date', 'address', 'gender']


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'full_name', 'grade', 'email', 'birth_date', 'address', 'gender']
