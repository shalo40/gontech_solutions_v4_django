from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Tecnico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar'))
