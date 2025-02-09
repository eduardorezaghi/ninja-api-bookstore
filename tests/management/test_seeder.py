import unittest
import unittest.mock as mock

class TestSeedData(unittest.TestCase):
    def setUp(self):
        self.mock_author = mock.patch('bookstore.management.seeder.Author.objects.create').start()
        self.mock_book = mock.patch('bookstore.management.seeder.Book.objects.create').start()
        self.mock_publisher = mock.patch('bookstore.management.seeder.Publisher.objects.create').start()
        self.mock_store = mock.patch('bookstore.management.seeder.Store.objects.create').start()

    def test_seed_data(self):
        from bookstore.management.seeder import seed_database

        mock_transaction = mock.MagicMock(autospec=True)
        mock_writer = mock.MagicMock(autospec=True)
        seed_database(authors=10, books=50, publishers=5, stores=8, writer=mock_writer, _faker=None, transaction=mock_transaction)
        calls = mock_writer.call_args_list
        
        mock_transaction.atomic.assert_called()
        self.mock_author.assert_called()
        self.mock_book.assert_called()
        self.mock_publisher.assert_called()
        self.mock_store.assert_called()
        
        assert len(calls) == 6
        assert any('Starting database seeding...' in str(call) for call in calls)
        assert any('Created 10 authors' in str(call) for call in calls)
        assert any('Created 5 publishers' in str(call) for call in calls)
        assert any('Created 8 stores' in str(call) for call in calls)
        assert any('Database seeding completed.' in str(call) for call in calls)


    def tearDown(self):
        mock.patch.stopall()