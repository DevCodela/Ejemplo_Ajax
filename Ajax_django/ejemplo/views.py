from django.views.generic import ListView
from django.http import HttpResponse
from .models import Autor,Libro
from django.core import serializers


class AutoresView(ListView):
	model = Autor
	template_name = 'libros.html'
	context_object_name = 'autores'


def busqueda_libros(request):
	if request.is_ajax():
		if request.method == 'GET':
			libros = Libro.objects.filter(autor__id = request.GET['id'])
			dato = serializers.serialize('json', libros)
	else:
		dato = False
	return HttpResponse(dato, content_type="application/json")


