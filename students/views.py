from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from students.models import Student
from students.forms import StudentCreateForm, StudentEditForm


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def register_teacher(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/students/')
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {'form': form})


def students_list_view(request):
    if request.method == 'GET':
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, 'students/students.html', context=context)


def student_detail_view(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id=id)
        context = {
            'student': student
        }
        return render(request, 'students/detail.html', context=context)


def student_create_view(request):
    if request.method == 'GET':
        context = {
            'form': StudentCreateForm
        }
        return render(request, 'students/create.html', context=context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = StudentCreateForm(data, files)
        if form.is_valid():
            Student.objects.create(
                photo=form.cleaned_data.get('photo'),
                full_name=form.cleaned_data.get('full_name'),
                email=form.cleaned_data.get('email'),
                birth_date=form.cleaned_data.get('birth_date'),
                address=form.cleaned_data.get('address'),
                gender=form.cleaned_data.get('gender'),
                grade=form.cleaned_data.get('grade')
            )
            return redirect('/students/')
        return render(request, 'students/create.html', context={'form': form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(f'/students/{student.id}', student_id=student_id)
    else:
        form = StudentEditForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})


def delete_student_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('/students/')
    return render(request, 'students/delete.html', {'student': student})
