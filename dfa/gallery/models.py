from django.db import models
from authentication.models import User


def productFile(instance, filename):
    return '/'.join(['gallery', str(instance.owner.email), filename])


class UserGallery(models.Model):
    image = models.ImageField(upload_to=productFile)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

