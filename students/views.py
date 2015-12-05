# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages




def list_view(request):
  try:
    id = request.GET['course_id']
    students = Student.objects.filter(courses=id)
    for student in students:
      student.courses_id = Course.objects.filter(student=student)  
    return render(request, 'students/list.html', {"student": students})
  except:
    students = Student.objects.all()
    for student in students:
      student.courses_id = Course.objects.filter(student=student)  
    return render(request, 'students/list.html', {"student": students})
  

def detail(request,sid):
  student = Student.objects.get(id=sid)
  student.courses_id=Course.objects.filter(student=student)  
  return render(request, 'students/detail.html', {"stud": student})


def create(request):
  form = StudentModelForm()
  if request.method == 'POST':
    form = StudentModelForm(request.POST)
    if form.is_valid():
      add_stud = form.save()
      messages.success(request, u'Student %s %s has been successfully added.' % (add_stud.name, add_stud.surname))
      return redirect('students:list_view')
  return render(request,'students/add.html',{'form':form})

def remove(request,sid):
  student = Student.objects.get(id=sid)
  message = u"%s %s" %(student.name, student.surname)
  if request.method == 'POST':
    student.delete()
    messages.success(request, u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
    return redirect('students:list_view')
  return render(request, 'students/remove.html', {'message': message})

def edit(request,sid):
  student = Student.objects.get(id=sid)
  if request.method == 'POST':
    form = StudentModelForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      messages.success(request, u'Info on the student has been sucessfully changed.')
      return redirect('students:list_view')
  else:
    form = StudentModelForm(instance=student)
  return render(request,'students/edit.html',{'form':form})