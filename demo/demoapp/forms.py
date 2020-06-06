from django import forms
from djgentelella.forms.forms import CustomForm
from .models import Foo
from djgentelella.widgets import numberknobinput as knobwidget


class FooModelForm(CustomForm, forms.ModelForm):
    class Meta:
        model = Foo
        fields = ('number_of_eyes', 
                  'speed_in_miles_per_hour',
                  'age')
        widgets = {
            'number_of_eyes': knobwidget.NumberKnobInput(attrs={}),
            'speed_in_miles_per_hour': knobwidget.NumberKnobInput(
                                            attrs={
                                                "data-min": 1,
                                                "data-step": 0.1,
                                                "data-max": 50
                                            }),
            'age': knobwidget.NumberKnobInput()
        }

class FooBasicForm(CustomForm, forms.Form):
    """creates a basic form with three widgets using different attrs"""
    age = forms.IntegerField(
            widget=knobwidget.NumberKnobInput(attrs={}), initial=15)
    speed_in_miles_per_hour = forms.FloatField(
                                widget=knobwidget.NumberKnobInput(attrs={
                                                          "data-min":1,
                                                          "data-step": 0.1,
                                                          "data-max":50}))
    number_of_eyes = forms.IntegerField(
                        widget=knobwidget.NumberKnobInput(attrs={
                                                  "data-min":1,
                                                  "steps": 0.1,
                                                  "data-max":50}))