from typing import List
from ninja import Router
from django.http import HttpRequest

from bookstore.api.schemas import BookResponse
from bookstore.models import Book

router = Router()

@router.get("/book/{book_id}", response=BookResponse)
async def book(request: HttpRequest, book_id: int):
    book = await Book.objects.aget(id=book_id)
    return BookResponse(
        id=book.id,
        created_at=book.created_at,
        updated_at=book.updated_at,
        is_deleted=book.is_deleted,
        title=book.title
    )

@router.get("/books", response=List[BookResponse])
async def books(request: HttpRequest) -> list[BookResponse]:
    params = request.GET.dict()
    print(params)

    books = [book async for book in Book.objects.filter(**params)]

    _books = []
    for book in books:
        _books.append(BookResponse(**book.__dict__))

    return _books

