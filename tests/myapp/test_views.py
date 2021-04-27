import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Route_list_view():
    instance1 = test_helpers.create_myapp_Route()
    instance2 = test_helpers.create_myapp_Route()
    client = Client()
    url = reverse("myapp_Route_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Route_create_view():
    created_by = test_helpers.create_myapp_AppUser()
    client = Client()
    url = reverse("myapp_Route_create")
    data = {
        "name": "text",
        "file": "aFile",
        "created_by": created_by.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Route_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_Route()
    url = reverse("myapp_Route_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Route_update_view():
    created_by = test_helpers.create_myapp_AppUser()
    client = Client()
    instance = test_helpers.create_myapp_Route()
    url = reverse("myapp_Route_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "file": "aFile",
        "created_by": created_by.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_AppUser_list_view():
    instance1 = test_helpers.create_myapp_AppUser()
    instance2 = test_helpers.create_myapp_AppUser()
    client = Client()
    url = reverse("myapp_AppUser_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_AppUser_create_view():
    client = Client()
    url = reverse("myapp_AppUser_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_AppUser_detail_view():
    client = Client()
    instance = test_helpers.create_myapp_AppUser()
    url = reverse("myapp_AppUser_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_AppUser_update_view():
    client = Client()
    instance = test_helpers.create_myapp_AppUser()
    url = reverse("myapp_AppUser_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
