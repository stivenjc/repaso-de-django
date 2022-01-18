from datetime import datetime

from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length = 150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        db_table = 'tipo'
        ordering = ['id']


class Categorias(models.Model):
    name = models.CharField(max_length = 150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'
        ordering = ['id']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categorias)
    name = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='Ndni', unique=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%/%m/%d', null=True, blank=True)
    avitae = models.ImageField(upload_to='avatar/%/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        db_table = 'empleado'
        ordering = ['id']