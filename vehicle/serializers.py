from rest_framework import serializers
from .models import BdVehicle, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='vehicle_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class BdVehicleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = BdVehicle
        fields = ('id','desc','amount','currency','vehicle_type','created_at','updated_at','image')
        expandable_fields = {'image': (ImageSerializer,{'many': True}) }


