# -*- coding: utf-8 -*-
"""
@author: admin
"""

# books.py

import uuid
from datetime import datetime
from models import Book
from storage import load_books, save_books

BOOKS_FILE = 'books.json'

def list_books():
    books = load_books()
    if not books:
        print("No books available in the library.")
        return

    print("\n📚 Available Books:")
    for book in books.values():
        print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Available: {book.available_copies}/{book.total_copies}")

def add_book():
    title = input("Book Title: ")
    author = input("Author: ")
    publication_year = input("Publication Year: ")
    
    
    try:
        total_copies = int(input("Total Copies: "))
    except ValueError:
        print("❌ Invalid input for total copies. Book not added.")
        return


    book = Book(
        id=str(uuid.uuid4()),
        title=title,
        author=author,
        publication_year=publication_year,
        total_copies=total_copies,
        available_copies=total_copies
    )

    books = load_books()
    books[book.id] = book
    save_books(books)
    print(f"✅ Book '{title}' added successfully!")

def view_books():
    books = load_data(BOOKS_FILE)

    if not books:
        print("📚 No books available.")
        return

    print("\nAvailable Books:")
    for book in books:
        status = "Available ✅" if book['is_available'] else "Borrowed ❌"
        print(f"📘 {book['title']} by {book['author']} ({book['publication_year']}) - {status}")
