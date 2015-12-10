# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentDetailView(DetailView):
  model = Student

class StudentListView(ListView):
  model = Student  
  #paginate_by = 2
  def get_queryset(self):
    id = self.request.GET.get('course_id',None)  
    if id:
      students = Student.objects.filter(courses=id)
    else:
      students = Student.objects.all()
    return students

#CreateView, UpdateView, DeleteView
class StudentCreateView(CreateView):
  model = Student
  
  def get_context_data(self, **kwargs):
    context = super(StudentCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Student registration'
    return context

  def form_valid(self,form):
    student = form.save()
    messages.success(self.request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
    return super(StudentCreateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
  model = Student
  success_url = reverse_lazy('students:list_view')
  
  def form_valid(self,form):
      student = form.save()
      messages.success(self.request, u'Info on %s %s has been sucessfully deleted.'  % (student.name, student.surname))
      return super(StudentDeleteView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(StudentDeleteView, self).get_context_data(**kwargs)
    student =  Student.objects.get(id=self.kwargs['pk'])
    context['title'] = 'Student info suppression'
    context['message'] ='%s %s' % (student.name, student.surname)
    
    return context
    

class StudentUpdateView(UpdateView):
  model = Student
  form_class = StudentModelForm
  template_name = 'students/edit.html'
  success_url = reverse_lazy('students:list_view')
  

  def get_context_data(self, **kwargs):
    context = super(StudentUpdateView, self).get_context_data(**kwargs)    
    context['title'] = 'Student info update'
    return context

  def form_valid(self,form):
    student = form.save()
    messages.success(self.request, u'Info on %s %s the student has been sucessfully changed.'  % (student.name, student.surname))
    return super(StudentUpdateView, self).form_valid(form)
