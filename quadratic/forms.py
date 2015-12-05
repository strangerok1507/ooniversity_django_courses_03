# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
  a = forms.IntegerField(label=u'Коеффициент а')
  b = forms.IntegerField(label=u'Коеффициент b')
  c = forms.IntegerField(label=u'Коеффициент с')


  def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return a