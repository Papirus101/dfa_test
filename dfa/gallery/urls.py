from django.urls import path

from .views import DeleteAllImage, UserPhotoList

app_name = 'gallery'
urlpatterns = [
    path('my/', UserPhotoList.as_view()),
    path('drop_all/', DeleteAllImage.as_view()),
]
