from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/user/', include('authentication.urls', namespace='authentication')),
    path('api/gallery/', include('gallery.urls', namespace='gallery'))
]
