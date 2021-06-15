from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientSerializer, ClientListSerializer, ClientDetailSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientSerializer.Meta.model.objects.all()
    serializer_class = ClientSerializer

    def list(self, request, *args, **kwargs):
        client = self.get_queryset()
        serializer = ClientListSerializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None,  *args, **kwargs):
        client = self.get_queryset().filter(id=pk).first()
        if client:
            serializer = ClientDetailSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

