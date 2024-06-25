from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import HistorialCliente

class HistorialClienteForm(forms.ModelForm):
    class Meta:
        model = HistorialCliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar'))
