from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.urls import reverse


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='grades_num')

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    grade = models.ManyToManyField(Grade, related_name='students_grades')
    address = models.TextField()
    gender = models.CharField(max_length=10)
    photo = models.ImageField( blank=True, null=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])
