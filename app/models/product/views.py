from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductListSerializer,  ProductDetailSerializer
from .models import Product


class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailedAPIView(APIView):
    def get(self, pk, request):
        product = Product.objects.filter(id=pk).first()
        if product:
            serializer = ProductDetailSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'message' : 'No such product'},
            status=status.HTTP_200_OK
        )

    def put(self, *args, **kwargs):
        request = kwargs['request']
        pk = kwargs['pk']
        product = Product.objects.filter(id=pk).first()
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'message' : 'No such product'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(id=pk).first()
        if product:
            product.save()
            return Response(status=status.HTTP_200_OK)
        return Response(
            {'message': 'No such product'},
            status=status.HTTP_400_BAD_REQUEST
        )
