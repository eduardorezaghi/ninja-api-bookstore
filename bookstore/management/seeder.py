from django.db import transaction
from django.utils import timezone
import random
from decimal import Decimal

from bookstore.models import Author, Book, Publisher, Store

def seed_database(
    authors=10,
    books=50,
    publishers=5,
    stores=8,
    writer: callable = None,
    _faker=None,
    transaction=transaction
):
    """Seed database with mock data"""
    if _faker:
        fake = _faker
    else:
        from faker import Faker
        fake = Faker()

    if writer:
        writer(f'Starting database seeding...')

    with transaction.atomic():
        # Create Authors
        _authors = []
        for _ in range(authors):
            author = Author.objects.create(
                name=fake.name(),
                birth_date=fake.date_between(start_date='-90y', end_date='-20y'),
                created_at=timezone.now(),
                updated_at=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            )
            _authors.append(author)

        if writer:
            writer(f'Created {len(_authors)} authors')

        # Create Books
        _books = []
        for author in _authors:
            for _ in range(random.randint(1, books)):
                book = Book.objects.create(
                    title=fake.catch_phrase(),
                    author=author,
                    published_date=fake.date_between(start_date='-10y', end_date='now'),
                    price=Decimal(random.uniform(9.99, 99.99)).quantize(Decimal('0.01')),
                    created_at=timezone.now(),
                    updated_at=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
                )
                _books.append(book)

        if writer:
            writer(f'Created {len(_books)} books')

        # Create Publishers
        _publishers = []
        for _ in range(publishers):
            publisher = Publisher.objects.create(
                name=fake.company(),
                created_at=timezone.now(),
                updated_at=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            )
            # Assign random books to publishers
            publisher.books.set(random.sample(_books, random.randint(5, len(_books) // 2)))
            _publishers.append(publisher)

        if writer:
            writer(f'Created {len(_publishers)} publishers')

        # Create Stores
        _stores = []
        for _ in range(stores):
            store = Store.objects.create(
                name=f"{fake.company()} Bookstore",
                created_at=timezone.now(),
                updated_at=fake.date_time_between(start_date='-1y', end_date='now')
            )
            # Assign random books and publishers to stores
            store.books.set(random.sample(_books, random.randint(10, len(_books) // 2)))
            store.publishers.set(random.sample(_publishers, random.randint(1, len(_publishers))))
            _stores.append(store)

        if writer:
            writer(f'Created {len(_stores)} stores')

        if writer:
            writer('Database seeding completed.')
