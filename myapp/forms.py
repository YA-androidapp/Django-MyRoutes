from django import forms
from django.core.files.storage import default_storage
from . import models
import os


class RouteForm(forms.ModelForm):
    class Meta:
        model = models.Route
        fields = [
            "name",
            "file",
        ]


class RouteMultipleUploadForm(forms.Form):
    name = forms.CharField(
        label='name',
        max_length=100,
        required=True,
    )
    file = forms.FileField(
        label='file',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    def save(self):
        upload_to="upload/files/"

        file_list = []
        for upload_file in self.files.getlist('file'):
            file_path = os.path.join(upload_to, upload_file.name)
            file_name = default_storage.save(models.custom_upload_to(self, file_path), upload_file)
            file_list.append(file_path)
        return file_list


class AppUserForm(forms.ModelForm):
    class Meta:
        model = models.AppUser
        fields = []


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = [
            "title",
            "image",
            "route",
        ]