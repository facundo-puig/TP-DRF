from rest_framework import serializers
from .models import Gasto


class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = [
            "id",
            "descripcion",
            "monto",
            "categoria",
            "fecha",
        ]
        read_only_fields = ["id","fecha"]