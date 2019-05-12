from rest_framework.decorators import api_view
from .models import Album
from .models import Song
from .models import Artist
from django.shortcuts import get_object_or_404
from .serializers import AlbumGetSerializer
from .serializers import SongBaseSerializer
from .serializers import ArtistSongSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def album_api(request, name):
    name = name.replace('_', ' ')

    if name == 'all':
        albums = Album.objects.all()
        return Response(AlbumGetSerializer(albums, many=True).data)
    else:
        album = get_object_or_404(Album, name__iexact=name)
        return Response(AlbumGetSerializer(album).data)


@api_view(['GET'])
def song_api(request, name):
    name = name.replace('_', ' ')
    song = get_object_or_404(Song, name__iexact=name)

    return Response(SongBaseSerializer(song).data)


@api_view(['GET'])
def artist_api(request, name):
    name = name.replace('_', ' ')

    if name == 'all':
        artists = Artist.objects.all()
        return Response(ArtistSongSerializer(artists, many=True).data)
    else:
        artist = get_object_or_404(Artist, name__iexact=name)
        return Response(ArtistSongSerializer(artist).data)
