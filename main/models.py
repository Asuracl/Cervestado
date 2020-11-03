from django.db import models

# Create your models here.
 
class User (models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    pas = models.CharField(max_length=10)


class Cerveza (models.Model):
    tipo = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()


