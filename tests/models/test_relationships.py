import pytest

import unittest
from datetime import datetime
from decimal import Decimal

from bookstore.models import Author, Book, Publisher, Store

@pytest.mark.django_db
class BookModelTest(unittest.TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Test Author",
            birth_date=datetime(1990, 1, 1)
        )
        
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            published_date=datetime(2023, 1, 1),
            price=Decimal("29.99")
        )

        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.publisher.books.add(self.book)

        self.store = Store.objects.create(name="Test Store")
        self.store.books.add(self.book)
        self.store.publishers.add(self.publisher)

    def test_book_creation(self):
        assert self.book.title == "Test Book"
        assert self.book.author.name == "Test Author"
        assert self.book.price == Decimal("29.99")

    def test_book_publisher_relationship(self):
        assert self.book.publisher_set.first() == self.publisher
        assert self.publisher.books.first() == self.book

    def test_book_store_relationship(self):
        assert self.book.store_set.first() == self.store
        assert self.store.books.first() == self.book

    def test_cascade_delete(self):
        author_id = self.author.id
        self.author.delete()
        with pytest.raises(Book.DoesNotExist):
            Book.objects.get(id=self.book.id)