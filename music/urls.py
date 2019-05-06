from django.urls import path
from .views import *


urlpatterns = [
    path('album/<slug:name>', album_api),
    path('song/<slug:name>', song_api),
    path('artist/<slug:name>', artist_api),
]
