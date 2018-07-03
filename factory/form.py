from django import forms
from .models import  Tarea

class TareaEditForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ('deadline', 'duration')
'''
    horas = forms.IntegerField()
    minutos = forms.IntegerField()

    def clean(self):
        cleaned_data = super(TareaEditForm, self).clean()
        horas = cleaned_data.get('horas')
        minutos = cleaned_data.get('munitos')
        if not horas and not minutos:
            raise forms.ValidationError('You have to write something!')
'''
