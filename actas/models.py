from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

######################################################################################################
# Login de usuario
from django.core.exceptions import ValidationError


class tipo_documento (models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class login_user(AbstractUser):

    tipo_documento_user = models.ForeignKey(tipo_documento, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

######################################################################################################
# ITEM

class crea_item (models.Model):
    numero_item= models.IntegerField()
    descripcion_item= models.CharField(max_length=200)
    ubicacion_item= models.CharField(max_length=200)
    unidad_item= models.CharField(max_length=10)
    cantidad_item= models.FloatField()
    valor_item= models.FloatField()
    fecha_realizacion_item= models.DateTimeField()

######################################################################################################
# CREADOR DE ACTOR
class tipo_actor (models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class actor(models.Model):
    nombre_actor= models.CharField(max_length=50)
    tipo_documento_actor= models.ForeignKey(tipo_documento, on_delete=models.CASCADE)
    numero_documento_actor= models.IntegerField()
    tipo_actor= models.ForeignKey(tipo_actor, on_delete=models.CASCADE)
    numero_telefono_actor= models.IntegerField()
    direccion_actor= models.CharField(max_length=50)

######################################################################################################
# ACTOR ###### QUEDA PENDIENTE POR DUDAS

class crea_proyecto(models.Model):

    #presupuesto_proye= models.Lista de Item 
    id_proyecto= models.CharField(max_length=10)
    nombre_proyecto= models.CharField(max_length=50)
    descripcion_proyecto= models.CharField(max_length=200)
    cliente_proyecto= actor() 
    supervisor_proyecto= actor()            
    contratante_proyecto= actor()        
    contratista_proyecto= [actor()]       


######################################################################################################
# CREA CONTRATISTA

class crea_contrati(models.Model):

    nuevo_contratista= actor()

######################################################################################################
# REGISTRO DE AVANCE

class registro_avance(models.Model):

    foto_avance= models.ImageField()
    capitulo_avance= models.CharField(max_length=200)
    subcapitulo_avance= models.CharField(max_length=200)
    actividad_avance= models.CharField(max_length=200)
  #  ele_avan= models.CheckBox()
    fec_avan= models.DateTimeField()


######################################################################################################
# REGISTRO DE ACTIVIDADES NO PRESUPUESTADAS

class registro_no_presupuestada(models.Model):

    capitulo_no_presupuestado= models.CharField(max_length=200)
    subcapitulo_no_presupuestado= models.CharField(max_length=200)
    actividad_no_presupuestado= models.CharField(max_length=200)
    elemento_no_presupuestado= models.CharField(max_length=200)

######################################################################################################
# REGISTRO DE ANTICIPO

class registro_anticipo (models.Model):
    fec_anti= models.DateTimeField()
    val_anti= models.FloatField()
    contratista_anticipo= actor()
    generador_acticipo= actor()