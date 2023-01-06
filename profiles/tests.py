from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest


# Create your tests here.
@pytest.mark.django_db
def test_profiles_index_page_code_status_and_title():
    client = Client()
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
    assert "<title>Profiles</title>" in response.content.decode()


@pytest.mark.django_db
def test_profiles_page_code_status_and_title():
    client = Client()
    user = User.objects.create(
        password="jqsldfycxheyu",
        username="username_title_test",
        email="test@test.fr"
    )
    Profile.objects.create(user=user, favorite_city="Wanaka")
    response = client.get(reverse("profile", kwargs={"username": "username_title_test"}))

    assert response.status_code == 200
    assert "<title>username_title_test</title>" in response.content.decode()
