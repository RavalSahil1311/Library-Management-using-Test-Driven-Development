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
    for book in books.values():
        books_list.append(book)
    return books_list


def borrow_books(book_id):
    if book_id in books:
        book = books[book_id]
        if book == False:
            return "Book Is not available to borrow"
        books.pop(book_id)
        books[book_id] = False
        return book
    return "Book not found to borrow"


def return_book(book_id, book):
    if book_id not in books:
        return "Book not found to return"
