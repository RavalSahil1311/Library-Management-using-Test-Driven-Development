import unittest
from Library import add_book, view_avalable_books, books


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        global books

    def test_add_book(self):
        book = ["12345679", "Wings of Fire", "APJ Abdul Kalam", 2008]
        self.assertEqual(add_book(book), book)
        self.assertEqual(add_book(book), "Book already exists")

    def test_view_available_books(self):
        books_list = []
        for book in books.values():
            books_list.append(book)
        self.assertEqual(view_avalable_books(), books_list)
