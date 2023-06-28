
from django.contrib import admin
from django.urls import path
from students.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('students/', students_list_view),
    path('students/<int:id>/', student_detail_view),
    path('student/create/', student_create_view),
]
