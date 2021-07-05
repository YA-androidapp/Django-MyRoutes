from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

import hashlib
import os
from datetime import datetime

def custom_upload_to(instance, filename):
    bname = os.path.basename(filename)
    if bname.startswith('hashed_') and len(bname) == (7 + 32 + 1 + 3):
        return filename
    else:
        current_time = datetime.now().strftime('%Y%m%d%H')
        pre_hash_name = '{}_{}'.format(current_time, os.path.basename(filename))
        extension = str(filename).split('.')[-1]
        hs_filename = 'hashed_{}.{}'.format(hashlib.md5(pre_hash_name.encode()).hexdigest(), extension)
        saved_path = 'upload/files/'
        filepath = '{}{}'.format(saved_path, hs_filename)
        print('instance, filename, filepath', instance, filename, filepath)
        return filepath


class Route(models.Model):

    # Relationships
    created_by = models.ForeignKey("myapp.AppUser", on_delete=models.CASCADE, related_name='routes')

    # Fields
    name = models.TextField(max_length=100)
    file = models.FileField(
        upload_to=custom_upload_to,
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



class Image(models.Model):

    # Relationships
    created_by = models.ForeignKey("myapp.AppUser", on_delete=models.CASCADE, related_name='images')
    route = models.ForeignKey("myapp.route", on_delete=models.CASCADE, related_name='images')

    # Fields
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    image = models.ImageField(upload_to=custom_upload_to)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("myapp_Image_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Image_update", args=(self.pk,))
