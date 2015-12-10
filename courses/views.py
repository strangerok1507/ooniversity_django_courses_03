from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from courses.models import Lesson,Course
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
  model = Course
  template_name = "courses/detail.html"

  def get_context_data(self, **kwargs):
    context = super(CourseDetailView, self).get_context_data(**kwargs)
    lessons = Lesson.objects.filter(course=self.object)
    context['lessons'] = lessons
    return context 

class CourseCreateView(CreateView):
  model = Course
  context_object_name = 'course'
  template_name = 'courses/add.html'
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(CourseCreateView, self).get_context_data(**kwargs)
    context['title'] = 'Course creation'
    return context 

  def form_valid(self,form):
    course = form.save()
    messages.success(self.request, 'Course %s has been successfully added.' % (course.name))
    return super(CourseCreateView, self).form_valid(form)

class CourseDeleteView(DeleteView):
  model = Course
  success_url = reverse_lazy('index')
  context_object_name = 'course'
  template_name = 'courses/remove.html'

  def form_valid(self,form):
      course = form.save()
      messages.success(self.request, u"Course %s has been deleted." % (course.name))
      return super(CourseDeleteView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(CourseDeleteView, self).get_context_data(**kwargs)
    course =  Course.objects.get(id=self.kwargs['pk'])
    context['title'] = 'Course deletion'
    return context

class CourseUpdateView(UpdateView):
  model = Course
  success_url = reverse_lazy('index')
  context_object_name = 'course'
  template_name = 'courses/edit.html'  
  def get_context_data(self, **kwargs):
      context = super(CourseUpdateView, self).get_context_data(**kwargs)
      context['title'] = 'Course update'
      return context

  def form_valid(self,form):
    course = form.save()
    messages.success(self.request, u"The changes have been saved.")
    return super(CourseUpdateView, self).form_valid(form)



def add_lesson(request,pk):  
  form = LessonModelForm(initial= {'course':cid} )
  if request.method == 'POST':
    form = LessonModelForm(request.POST)
    if form.is_valid():
      add_lesson = form.save();
      messages.success(request, u"Lesson %s has been successfully added." % (add_lesson.subject))
      return redirect('courses:detail',cid)
  return render(request,'courses/add_lesson.html',{'form':form})