from rest_framework import serializers

from .models import UserGallery

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['pk', 'image', ]
        model = UserGallery
