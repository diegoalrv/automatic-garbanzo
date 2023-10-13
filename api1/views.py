from rest_framework import viewsets
from .serializers import CatalogoSerializer
from .models import Catalogo2

from django.http import HttpResponse
from rest_framework.response import Response


class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo2.objects.all()
    serializer_class = CatalogoSerializer

class TestModelView(viewsets.ModelViewSet):
    serializer_class = CatalogoSerializer

    def get_queryset(self):
        value = self.kwargs.get('value')  # Obtén el valor del parámetro de la URL
        queryset = Catalogo2.objects.filter(tematica__icontains=value)
        print(queryset.count())
        return queryset
        
    
    
    
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
     





