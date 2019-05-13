from rest_framework import serializers
from .models import Album
from .models import Song
from .models import Artist


class ArtistBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', 'image_url')


class ArtistSongSerializer(ArtistBaseSerializer):
    songs = serializers.SerializerMethodField()

    def get_songs(self, obj):
        songs = Song.objects.filter(artists__name=obj.name)
        return SongBaseSerializer(songs, many=True).data

    class Meta(ArtistBaseSerializer.Meta):
        fields = ('id', 'name', 'songs', 'image_url')


class SongBaseSerializer(serializers.ModelSerializer):
    artists = ArtistBaseSerializer(many=True)
    album = serializers.SlugField()

    class Meta:
        model = Song
        fields = ('id', 'name', 'artists', 'album')


class SongAlbumSerializer(SongBaseSerializer):

    class Meta(SongBaseSerializer.Meta):
        fields = ('id', 'name', 'artists')


class AlbumGetSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    def get_songs(self, obj):
        songs = Song.objects.filter(album__name=obj.name)
        return SongAlbumSerializer(songs, many=True).data

    class Meta:
        model = Album
        fields = ('id', 'name', 'songs', 'image_url')