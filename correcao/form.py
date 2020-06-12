from django import forms
from .models import Texto

class TextoForm (forms.Form):
    class Meta:
        fields = ['situacao']
        model = Texto