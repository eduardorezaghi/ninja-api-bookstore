import datetime
import pytest

import unittest
from bookstore.models import Author

from unittest import mock


@pytest.mark.django_db
class TestAuthorModel(unittest.TestCase):
    def setUp(self):
        self.authors = [
            Author(name='John Doe'),
            Author(name='Jane Doe'),
        ]

    def test_author_model(self):
        Author.objects.bulk_create(self.authors)

        assert Author.objects.count() == 2
        assert Author.objects.get(name='John Doe')
        assert Author.objects.get(name='Jane Doe')
        assert Author.objects.get(name='John Doe').created_at is not None
        assert Author.objects.get(name='John Doe').updated_at is None
        assert Author.objects.get(name='John Doe').is_deleted is False

    def test_author_model_birthdate_custom(self):
        _author = Author.objects.create(name='John Doe', birth_date=datetime.date(1990, 1, 1))

        author = Author.objects.get(name='John Doe')
        
        assert author.birth_date == _author.birth_date
        assert author.birth_date == datetime.date(1990, 1, 1)

