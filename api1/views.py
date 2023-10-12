from rest_framework import viewsets
from .serializers import CatalogoSerializer
from .models import Catalogo2


class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo2.objects.all()
    serializer_class = CatalogoSerializer








