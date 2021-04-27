from django import forms
from . import models


class RouteForm(forms.ModelForm):
    class Meta:
        model = models.Route
        fields = [
            "name",
            "file",
        ]


class AppUserForm(forms.ModelForm):
    class Meta:
        model = models.AppUser
        fields = []
