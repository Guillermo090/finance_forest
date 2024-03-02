from django.db import models

# Create your models here.
class ClCliente(models.Model):
    rut = models.CharField(max_length=150,null=True,blank=True)
    nombres = models.CharField(max_length=150,null=True,blank=True)
    apellidos = models.CharField(max_length=150,null=True,blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)