from rest_framework import serializers
from movies.models import Movie
from .models import Rating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        choices=Rating.choices, default=Rating.G, allow_null=True
    )
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
