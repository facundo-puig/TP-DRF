from rest_framework import serializers
from .models import Gasto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        read_only_fields = ["id"]

class GastoPublicSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Gasto
        fields = ["id", "descripcion", "monto", "categoria", "fecha"]
        read_only_fields = ["id", "fecha"]

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ["id", "descripcion", "monto", "categoria", "fecha"]
        read_only_fields = ["id","fecha"]