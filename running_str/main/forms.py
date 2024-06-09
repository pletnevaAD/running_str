from django import forms
from .models import UsersRequest
from colorfield.widgets import ColorWidget

class RunningStrForm(forms.ModelForm):
    class Meta:
        model = UsersRequest
        fields =  ['text', 'background_color', 'text_color'] 
        labels = {
            'text': 'Введите текст',
            'background_color': 'Выберите цвет фона',
            'text_color': 'Выберите цвет текста'
        }
        widgets = {
            'background_color': ColorWidget,
            'text_color': ColorWidget
        }
