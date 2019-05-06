from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Playlist
from .serializers import PlaylistBaseSerializer as PlaylistSerializer


@api_view(['GET'])
def playlist_api(request, name):
    name = name.replace('_', ' ')
    playlist = get_object_or_404(Playlist, name__iexact=name)

    return Response(PlaylistSerializer(playlist).data)


