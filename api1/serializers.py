from rest_framework import serializers
from .models import Catalogo2

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Catalogo2
        fields = '__all__'