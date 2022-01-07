from django.db import models

# Create your models here.
class Empresa(models.Model):
    #columna = DiferentesTiposDeDatos
    #maximo caracteres es 20
    #enteros
    #MODEL FIELDS django
    nombre = models.CharField(max_length=90)
    fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
        #que se vea el nombre en la pagina

############new tabla

class Lenguaje(models.Model):
        nombre = models.CharField(max_length=90)
        creador = models.CharField(max_length=90, null=True)
        def __str__(self):
            return self.nombre

####nueva tabla
class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,related_name="empleados")
    lenguaje = models.ManyToManyField(Lenguaje)

    def __str__(self):
        return self.nombre
