import unittest
from Library import add_book, view_avalable_books, borrow_books, books


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

    def test_borrow_books(self):
        total_books = len(view_avalable_books())
        add_book(
            ["987654321", "Adventures of Sherlock Holmes", "Benedict CumberBatch", 2012]
        )
        self.assertEqual(
            borrow_books("987654321"),
            [
                "987654321",
                "Adventures of Sherlock Holmes",
                "Benedict CumberBatch",
                2012,
            ],
        )
        self.assertEqual(borrow_books("12345609"), "Book not found to borrow")
        self.assertEqual(borrow_books("987654321"), "Book Is not available to borrow")
