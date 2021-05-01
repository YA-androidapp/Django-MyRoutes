from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class Route(models.Model):

    # Relationships
    created_by = models.ForeignKey("myapp.AppUser", on_delete=models.CASCADE, related_name='routes')

    # Fields
    name = models.TextField(max_length=100)
    file = models.FileField(
        upload_to="upload/files/",
        validators=[FileExtensionValidator(['kml', ])],
    )
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_Route_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Route_update", args=(self.pk,))


class AppUser(AbstractUser):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("myapp_AppUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_AppUser_update", args=(self.pk,))
