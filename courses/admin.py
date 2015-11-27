from django.contrib import admin
from courses.models import Course,Lesson

class LessonAdmin(admin.ModelAdmin):
  list_display=['order','subject','course']

class CourseAdmin(admin.ModelAdmin):
  list_filter = ('name','short_description')

admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)
