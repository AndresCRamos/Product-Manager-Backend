from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import ProductListSerializer,  ProductSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()
    tag = ['product']

    def list(self, request, *args, **kwargs):
        products = ProductListSerializer.Meta.model.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        product = ProductSerializer.Meta.model.objects.filter(id=pk).first()
        serializer = ProductDetailSerializer(product)
        if product:
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
