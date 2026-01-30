from django.shortcuts import render
from django.views.generic import ListView

from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    # context_object_name = 'lista'
        
# 1.- Lista todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
