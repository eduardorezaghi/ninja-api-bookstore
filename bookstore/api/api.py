from ninja import NinjaAPI, Router
from django.http import HttpRequest
import pytest

from bookstore.api.schemas import HelloResponse

register = NinjaAPI()
router = Router()

@router.get("/hello", response=HelloResponse)
def hello(request: HttpRequest):
    print(request)
    return HelloResponse(
        msg="Hello World"
    )