from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .registro import RegistroFormulario

def registro_caminata(request):
	registro = RegistroFormulario(request.POST or None)

	

	if request.method == 'POST' and form.is_valid():
		usuario = registro.cleaned_data.get('nombre')
		email = registro.cleaned_data.get('email')
		distancia = registro.cleaned_data.get('distancia')
		messages.success(request, "{} su registro se ha guardado".format(RegistroFormulario.nombre))


	return render(request, 'registro.html',{})

