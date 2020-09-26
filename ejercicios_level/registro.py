from django import forms

class RegistroFormulario(forms.Form):
	nombre = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	distancia = forms.FloatField(required=True)