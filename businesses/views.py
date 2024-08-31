from rest_framework import viewsets
from businesses.models import Business
from businesses import serializers


class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BusinessSerializer

    def get_queryset(self):
        return Business.objects.all()
