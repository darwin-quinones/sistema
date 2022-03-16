from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.db import connection
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    ## guardar datos incluye files
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    # se obtienen los datos segun el id
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    
    # actualizar cambios
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def borrar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros') # redireccionar a la funcion libros
    
    
def query_mysql(request, id):
    
    # de esta forma podemos hacer consultas mysql
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM libreria_libro WHERE id= %s', [id])
    row = cursor.fetchone()
    formulario = row
    
    print(formulario)
    return render(request, 'libros/mysql.html', {'formulario': formulario})

def mysql_function(request, id):
    # de esta forma se hace consultas con una funcion
    def mysql_query():
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM libreria_libro WHERE id= %s', [id])
            row = cursor.fetchone()
        return row
    libro = mysql_query()
    
    print(libro)
    return render(request, 'libros/mysql.html', {'libro':libro})