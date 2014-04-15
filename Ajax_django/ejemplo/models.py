from django.db import models

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()

	def __unicode__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	fecha_publicacion = models.DateField()
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
		return self.titulo