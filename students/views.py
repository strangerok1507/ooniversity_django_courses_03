# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentForm
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
  form = StudentForm()
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      add_stud = form.save()
      messages.success(request, u'Студент %s %s успешно добавлен.' % (add_stud.name, add_stud.surname))
      return redirect('students:list_view')
  else:
    return render(request,'students/add.html',{'form':form})

def remove(request,sid):
  student = Student.objects.get(id=sid)
  message = u"%s %s" %(student.name, student.surname)
  if request.method == 'POST':
    student.delete()
    messages.success(request, u"Студент %s %s успешно удален." % (student.name, student.surname))
    return redirect('students:list_view')
  return render(request, 'students/remove.html', {'message': message})

def edit(request,sid):
  student = Student.objects.get(id=sid)
  if request.method == 'POST':
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      messages.success(request, u'Информация о студенте успешно обновлена.')
      return redirect('students:list_view')
  else:
    form = StudentForm(instance=student)
    return render(request,'students/edit.html',{'form':form})