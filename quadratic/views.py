# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse



def discr(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  d=(b*b)-(4*a*c)
  return d


def deq(request,a,b):
  x=-float(b)/(2*float(a))
  x= round(x,2)
  t=u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %d' % float(x)
  return t


def dbig(request,a,b,c):
  a=float(a)
  b=float(b)
  c=float(c)
  x1=(-b+((b*b-4*a*c)**(1/2.0)))/2*a
  x2=(-b-((b*b-4*a*c)**(1/2.0)))/2*a
  x1=str(round(x1,2))
  x2=str(round(x2,2))
  t=u'Квадратное уравнение имеет два действительных корня: x1 = %s x2 = %s ' % (x1,x2)
  return t

def quadratic_results(request):
  result={}
  error={}
  a=request.GET['a']
  b=request.GET['b']
  c=request.GET['c']  
  zn ={'a':a,'b':b,'c':c}
  err={}
  for i in sorted(zn.keys()):
    t='error_%s' % i
    try:
      zn[i]=int(zn[i])
      if i=='a' and zn[i]==0:
          zn[t]=u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
          err['flag']=1
    except Exception:
      if zn[i]=='':
        zn[t]=u'коэффициент не определен'  
        err['flag']=1
      else:
        zn[t]=u'коэффициент не целое число'
        err['flag']=1
  
  if err.values() ==[]:
    d=discr(request,a,b,c)
    zn['d']=int(d)
    if zn['d']==0:
      zn['resh']=deq(request,a,b)    
    elif zn['d']<0:
      zn['error_d']=u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
      zn['resh']=dbig(request,a,b,c)


  #context = RequestContext(request, {
  #      'zn':zn,'err':err,'d':d,'errd':errd
  #  })
      
  #template = loader.get_template('results.html')
  #return HttpResponse(template.render(context))
  return render(request,'results.html',zn)