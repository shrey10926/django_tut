from django.forms import ModelForm
from django import forms
from iris.models import IrisModel


class IrisForm(ModelForm):
    
    sepal_length = forms.DecimalField(max_digits = 6, decimal_places = 6)
    sepal_width = forms.DecimalField(max_digits = 6, decimal_places = 6)
    petal_length = forms.DecimalField(max_digits = 6, decimal_places = 6)
    petal_width = forms.DecimalField(max_digits = 6, decimal_places = 6)
    
    class Meta:
        model = IrisModel
        fields = ['sepal_length', 'sepal_width',
                  'petal_length', 'petal_width']
















