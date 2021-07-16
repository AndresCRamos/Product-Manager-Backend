from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import ZoneSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    serializer_class = ZoneSerializer
    queryset = ZoneSerializer.Meta.model.objects.all()
    tag = ['zone']
