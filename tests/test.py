import unittest
from Library import add_book, books


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        global books

    def test_add_book(self):
        book = ["12345679", "Wings of Fire", "APJ Abdul Kalam", 2008]
        self.assertEqual(add_book(book), book)
