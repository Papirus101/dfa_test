from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.mixins import Response, status

from .serializers import GallerySerializer
from .models import UserGallery
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserPhotoList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GallerySerializer

    def get_queryset(self):
        return UserGallery.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        product = UserGallery.objects.create(image=file, owner=request.user)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        image_id = request.data.get('id')
        if not isinstance(image_id, int):
            return Response({'error': 'id must be a number'}, status=status.HTTP_400_BAD_REQUEST)
        image = UserGallery.objects.filter(pk=image_id)
        if len(image) == 0:
            return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)
        if image[0].owner != request.user:
            return Response({'error': 'user is not owner this image'}, status=status.HTTP_403_FORBIDDEN)
        image[0].delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteAllImage(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        UserGallery.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
