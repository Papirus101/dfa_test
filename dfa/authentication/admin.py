from django.contrib import admin
from .models import User
from gallery.models import UserGallery

class GalleryInline(admin.TabularInline):
    fk_name = 'owner'
    model = UserGallery


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
