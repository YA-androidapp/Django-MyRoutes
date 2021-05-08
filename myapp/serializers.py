from rest_framework import serializers

from . import models


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Route
        fields = [
            "name",
            "file",
            "last_updated",
            "created",
        ]

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AppUser
        fields = [
            "last_updated",
            "created",
        ]


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = [
            "title",
            "created",
            "last_updated",
            "image",
        ]
