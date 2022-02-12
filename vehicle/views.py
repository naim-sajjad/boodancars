from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BdVehicleSerializer, ImageSerializer
from .models import BdVehicle,Image
from rest_flex_fields.views import FlexFieldsModelViewSet
from .paginations import CustomPagination
from django.db.models import Q

class BdVehicleViewSet(viewsets.ModelViewSet):
    queryset = BdVehicle.objects.all().order_by('created_at')
    serializer_class = BdVehicleSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        queryset = BdVehicle.objects.all().order_by('created_at')
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            queryset = BdVehicle.objects.filter(Q(desc__icontains=keyword) | Q(amount__icontains=keyword))
        return queryset;

class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
