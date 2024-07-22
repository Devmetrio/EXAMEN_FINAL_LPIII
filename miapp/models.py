from django.db import models

# Create your models here.
class AMES_Persona(models.Model):
    select_sexo = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer')
    )
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=8, choices=select_sexo)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)
