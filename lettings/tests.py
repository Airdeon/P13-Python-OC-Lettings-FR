from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting
import pytest


# Create your tests here.
@pytest.mark.django_db
def test_letting_index_page_code_status_and_title():
    client = Client()
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert "<title>Lettings</title>" in response.content.decode()


@pytest.mark.django_db
def test_letting_page_code_status_and_title():
    client = Client()
    address = Address.objects.create(
        number=8, street="street_test",
        city="city_test",
        state="state_test",
        zip_code=12345,
        country_iso_code="033"
    )
    Letting.objects.create(title="test_title", address=address)
    response = client.get(reverse("letting", kwargs={"letting_id": 1}))

    assert response.status_code == 200
    assert "<title>test_title</title>" in response.content.decode()
