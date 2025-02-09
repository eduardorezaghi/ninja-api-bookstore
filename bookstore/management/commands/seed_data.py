from django.core.management.base import BaseCommand
from bookstore.management import seed_database


class Command(BaseCommand):
    help = 'Seed database with mock data'

    def add_arguments(self, parser):
        parser.add_argument('--authors', type=int, default=10, help='Number of authors to create')
        parser.add_argument('--books', type=int, default=50, help='Number of books per author')
        parser.add_argument('--publishers', type=int, default=5, help='Number of publishers')
        parser.add_argument('--stores', type=int, default=8, help='Number of stores')

    def handle(self, *args, **options):
        seed_database(
            authors=options['authors'],
            books=options['books'],
            publishers=options['publishers'],
            stores=options['stores'],
            writer=self.stdout.write
        )