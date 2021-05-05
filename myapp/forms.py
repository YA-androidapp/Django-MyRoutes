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
            file_name = default_storage.save(os.path.join(upload_to, upload_file.name), upload_file)
            # file_path = default_storage.url(file_name)
            file_list.append(file_name)
        return file_list


class AppUserForm(forms.ModelForm):
    class Meta:
        model = models.AppUser
        fields = []
