from rest_framework import generics
from .models import Gasto, Categoria
from .serializers import GastoSerializer, GastoPublicSerializer, CategoriaSerializer


class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class GastoListCreateView(generics.ListCreateAPIView):
    queryset = Gasto.objects.all().select_related("categoria")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GastoPublicSerializer
        return GastoSerializer

class GastoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all().select_related("categoria")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GastoPublicSerializer
        return GastoSerializer