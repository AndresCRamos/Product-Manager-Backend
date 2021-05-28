from rest_framework import status
from rest_framework.views import Response, APIView
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierAPIView(APIView):
    def get(self, request):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierDetailedAPIView(APIView):
    def get(self, request, pk=None):
        supplier = Supplier.objects.filter(id=pk).first()
        if supplier:
            serializer = SupplierSerializer(supplier)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'message': 'No such supplier'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        supplier = Supplier.objects.filter(id=pk).first()
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'message': 'No such product'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk=None):
        supplier = Supplier.objects.filter(id=pk).first()
        if supplier:
            supplier.delete()
            return Response(
                {'message' : 'Supplier deleted'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'No such supplier'},
            status=status.HTTP_400_BAD_REQUEST
        )
