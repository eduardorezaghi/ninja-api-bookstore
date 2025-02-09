import asyncio
from ninja import NinjaAPI
from django.http import HttpRequest

from bookstore.api.schemas import HelloResponse
from bookstore.api.books import books_router

api = NinjaAPI()

@api.get("/hello", response=HelloResponse)
def hello(request: HttpRequest):
    print(request)
    return HelloResponse(
        msg="Hello World"
    )

@api.get("/say-after", response=HelloResponse)
async def say_after(request: HttpRequest, delay:int, msg: str):
    await asyncio.sleep(delay)
    return HelloResponse(
        msg=msg
    )

# Routers.
api.add_router("/books", books_router)