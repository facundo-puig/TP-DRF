from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Gasto
from .serializers import GastoSerializer


@api_view(['GET', 'POST'])
def gasto_list(request):
    if request.method == "GET":
        gastos = Gasto.objects.all()
        serializer = GastoSerializer(gastos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = GastoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Gasto agregado"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )
        
@api_view(["GET", "PUT", "DELETE"])
def gasto_detail(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    
    if request.method == "GET":
        serializer = GastoSerializer(gasto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = GastoSerializer(gasto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Gasto Actualizado"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se Actualizó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if request.method == "DELETE":
        gasto.delete()
        return Response(
            {"mensaje": "Gasto Borrado"},
            status=status.HTTP_200_OK,
        )
