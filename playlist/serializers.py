from rest_framework import serializers
from music.serializers import SongBaseSerializer
from music.models import Song
from .models import Playlist


class PlaylistBaseSerializer(serializers.ModelSerializer):

    songs = serializers.SerializerMethodField()

    def get_songs(self, obj):
        songs = Song.objects.filter(playlist__name=obj.name)
        return SongBaseSerializer(songs, many=True).data

    class Meta:
        model = Playlist
        fields = ('name', 'songs')