from django.shortcuts import render
from courses.models import Lesson,Course



def detail(request,cid):
  course=Course.objects.get(id=cid)
  lessons=Lesson.objects.filter(course_id=cid)
  return render(request, 'courses/detail.html', {"lessons": lessons,"course":course})
  