from django.test import TestCase
from ninja.testing import TestClient
import pytest
from bookstore.api.base import base_api

import unittest.mock as mock

@pytest.mark.usefixtures("test_client")
class TestBaseRoutes(TestCase):
    def test_get_hello_should_return_hello_world(self):
        response = self.client.get("/api/hello")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

    @mock.patch("asyncio.sleep", return_value=None)
    def test_say_after_should_return_msg_after_delay(self, mock_sleep):
        delay=10
        message="Hello"
        response = self.client.get(f"/api/say-after?delay={delay}&msg={message}")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello"}
        assert mock_sleep.called