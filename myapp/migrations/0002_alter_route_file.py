# Generated by Django 3.2 on 2021-04-29 03:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='file',
            field=models.FileField(upload_to='upload/files/', validators=[django.core.validators.FileExtensionValidator(['kml'])]),
        ),
    ]
