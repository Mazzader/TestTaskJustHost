from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import VPS
from api.serializers import VPSSerializer, VPSChangeStatusSerializer


class VPSAPIView(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    serializer_class = VPSSerializer
    queryset = VPS.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram', 'hdd', 'status']


class VPSChangeStatusView(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = VPSChangeStatusSerializer
    queryset = VPS.objects.all()
    http_method_names = ['patch']
