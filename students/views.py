from django.shortcuts import render
from students.models import Student
from courses.models import Course
import pickle

def list_view(request):
  try:
    id = request.GET['course_id']
    students = Student.objects.filter(courses=id)
    for student in students:
      student.courses_id = Course.objects.filter(student=student)  
    print 'try'
    return render(request, 'students/list.html', {"student": students})
  except:
    students = Student.objects.all()
    for student in students:
      student.courses_id = Course.objects.filter(student=student)  
    return render(request, 'students/list.html', {"student": students})
  

def detail(request,sid):
  student = Student.objects.filter(id=sid)
  student.courses_id=Course.objects.filter(student=student)
  return render(request, 'students/detail.html', {"student": student})
  