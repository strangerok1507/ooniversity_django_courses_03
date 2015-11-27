from django.contrib import admin

from students.models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display=['name','surname','courses_display']


admin.site.register(Student,StudentAdmin)
