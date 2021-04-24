from rest_framework import serializers
from .models import IMAGES
from django import forms

class IMAGE_serializer(serializers.Serializer):
    class Meta:
        model = IMAGES
        fields = '__all__'

class universal_serializer(forms.Form):
    pass


# class image_serializer2(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = IMAGES
#         fields = '__all__'

