from rest_framework import viewsets
from .serializers import CatalogoSerializer
from .models import Catalogo2

from django.http import HttpResponse



class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo2.objects.all()
    serializer_class = CatalogoSerializer

# def catalogobytematica(request,tematica):
#     busqueda = 'da'
#     objetos = Catalogo2.objects.filter(tematica__icontains=tematica)
#     i = 0
#     for obj in objetos:
#         i += 1
#     print(i)
#     return HttpResponse('hola')
    
    
def catalogoByColumn(request,column,value):
    if column == 'tematica':
        objetos = Catalogo2.objects.filter(tematica__icontains=value)
        return HttpResponse('hola')
    if column == 'nombre':
        objetos = Catalogo2.objects.filter(nombre__icontains=value)
        return HttpResponse('hola')
    if column == 'formato':
        objetos = Catalogo2.objects.filter(formato__icontains=value)
        return HttpResponse('hola')
    else:
        return HttpResponse('no esta disponible esa columna')
     





