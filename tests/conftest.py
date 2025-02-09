import pytest


@pytest.fixture(autouse=True)
def test_client(request):
    from ninja.testing import TestClient
    from bookstore.api import base_api

    request.cls.client = TestClient(base_api)