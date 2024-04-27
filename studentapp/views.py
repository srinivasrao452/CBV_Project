
from django.shortcuts import render
from studentapp.models import Student
from django.views.generic import (
    ListView, DetailView,CreateView,UpdateView,DeleteView
)

class StudentListView(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'studentapp/student_list.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ['sname', 'marks', 'city','mobile']
    context_object_name = 'form'
    template_name = 'studentapp/student_from.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['sname', 'marks', 'city','mobile']
    context_object_name = 'form'
    template_name = 'studentapp/student_from.html'


class StudentDeleteView(DeleteView):
    model = Student

    success_url = '/students/list/'

    context_object_name = 'student'
    template_name = 'studentapp/student_confirm_delete.html'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'studentapp/student_detail.html'











