from django.test import Client
from django.urls import reverse

import pytest


# Create your tests here.
@pytest.mark.django_db
def test_index_page_code_status_and_title():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in response.content.decode()
