from django.urls import path
from .views import *


urlpatterns = [
    path('<slug:name>', playlist_api)
]