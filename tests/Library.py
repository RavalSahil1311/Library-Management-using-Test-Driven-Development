from typing import List

books = {
    "98765432": ["98765432", "To Kill a Mockingbird", "Harper Lee", 1960],
}


def add_book(book: List):
    id = book[0]
    if id in books:
        return "Book already exists"
    books[id] = book
    return books[id]


def view_avalable_books():
    books_list = []
