from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "duration",
            "album_id",
        ]
        read_only_fields = ["album_id"]

