from django.shortcuts import render
from courses.models import Lesson,Course
from coaches.models import Coach



def detail(request,cid):
  coach={}
  assistant={}
  course=Course.objects.get(id=cid)
  coach['fio']=course.coach.user.get_full_name()
  assistant['fio']=course.assistant.user.get_full_name()
  coach['id']=course.coach.id
  assistant['id']=course.assistant.id
  coach['description']=course.coach.description
  assistant['description']=course.assistant.description
  lessons=Lesson.objects.filter(course_id=cid)
  return render(request, 'courses/detail.html', {"lessons": lessons,"course":course,'coach':coach,'assistant':assistant})
  