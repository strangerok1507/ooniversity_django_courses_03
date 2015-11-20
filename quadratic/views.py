# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader


def discr(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  d=(b*b)-(4*a*c)
  return d


def deq(request,a,b):
  x=-float(b)/(2*float(a))
  t=u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %d' % x
  return t


def dbig(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  x1=(-b+((b*b-4*a*c)**(1/2.0)))/2*a
  x2=(-b-((b*b-4*a*c)**(1/2.0)))/2*a
  x1=str(round(x1,2))
  x2=str(round(x2,2))
  t=u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 =%s x2 =%s ' % (x1,x2)
  return t

def results(request):
  result={}
  error={}
  a=request.GET['a']
  b=request.GET['b']
  c=request.GET['c']  
  zn ={'a':a,'b':b,'c':c}
  err={}
  for i in sorted(zn.keys()):
    try:
      zn[i]=int(zn[i])
    except Exception:
      if zn[i].isdigit():
        zn[i]=zn[i]
        if i=='a' and zn[i]==0:
          err[i]=u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
      elif zn[i]=='':
        err[i]=u'коэффициент не определен'  
      else:
        err[i]=u'коэффициент не целое число'
  if err.values() ==[]:
    d=discr(request,a,b,c)
    d=int(d)
    print type(d)
    print d
    if d<0:
      errd=u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif d==0:
      errd=deq(request,a,b)
    else:
      errd=dbig(request,a,b,c)
    print errd
  else:
    d=''
    errd=''
  context = RequestContext(request, {
        'zn':zn,'err':err,'d':d,'errd':errd
    })
      
  template = loader.get_template('results.html')
  return HttpResponse(template.render(context))
