from django.test import TestCase
from ninja.testing import TestClient
from bookstore.api import router

class HelloTest(TestCase):
    def setUp(self):
        self.client = TestClient(router)
    
    def test_get_hello_should_return_hello_world(self):
        response = self.client.get("/hello")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}