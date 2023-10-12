from rest_framework import viewsets
from .serializers import CatalogoSerializer
from .models import Catalogo2

from django.http import HttpResponse



class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo2.objects.all()
    serializer_class = CatalogoSerializer

# class CatalogoByTematicaViewSet(viewsets.ModelViewSet,):
#     queryset = Catalogo2.objects.filter(tematica__icontains=)


def catalogobytematica(request):
    busqueda = 'da'
    objetos = Catalogo2.objects.filter(tematica__icontains=busqueda)
    i = 0
    for obj in objetos:
        i += 1
    print(i)
    return HttpResponse('hola')
    
    






