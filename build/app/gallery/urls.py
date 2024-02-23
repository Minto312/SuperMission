from django.urls import path
from .views import map, viewer
from .apps import GalleryConfig

app_name = GalleryConfig.name

urlpatterns = [
    path('', map, name='map'),
    path('gallery/<str:view_name>', viewer, name='viewer')
]