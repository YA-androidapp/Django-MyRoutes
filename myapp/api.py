from rest_framework import viewsets, permissions

from . import serializers
from . import models


class RouteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Route class"""

    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the AppUser class"""

    queryset = models.AppUser.objects.all()
    serializer_class = serializers.AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]
