# -*- coding: utf-8 -*-
"""
@author: admin
"""

# loans.py

from datetime import datetime
from models import Loan
from storage import load_books, save_books,load_loans, save_loans

def borrow_book(user_email):
    books = load_books()
    loans = load_loans()

    print("\nBooks Available to Borrow:")
    available_books = [book for book in books.values() if book.available_copies > 0]

    if not available_books:
        print("❌ No books available for borrowing.")
        return
    
    print("\nBooks Available to Borrow:")

    for idx, book in enumerate(available_books):
        print(f"{idx + 1}. {book.title} by {book.author} (Available copies: {book.available_copies})")


    choice = int(input("Enter the number of the book you want to borrow: ")) - 1

    if choice < 0 or choice >= len(available_books):
        print("❌ Invalid choice.")
        return

    selected_book = available_books[choice]

    # Update book availability
    selected_book.available_copies -= 1   

    # Create loan record
    loan = Loan(
        book_id=selected_book.id,
        member_id=user_email,
        issue_date=datetime.now().date(),
        return_date=None
    )
    loans.append(loan)

    # Save updates
    save_books(books)
    save_loans(loans)

    print(f"✅ You have borrowed '{selected_book.title}' successfully!")

def return_book(user_email):
    books = load_books()
    loans = load_loans()
    
    user_loans = [loan for loan in loans if loan.member_id == user_email and loan.return_date is None]


    if not user_loans:
        print("📭 No borrowed books to return.")
        return

    print("\nYour Borrowed Books:")
    for idx, loan in enumerate(user_loans):
        book = books[loan.book_id]
        print(f"{idx + 1}. {book.title} by {book.author}")

    choice = int(input("Enter the number of the book you want to return: ")) - 1

    if choice < 0 or choice >= len(user_loans):
        print("❌ Invalid choice.")
        return

    selected_loan = user_loans[choice]
    selected_loan.return_date = datetime.now().date()

    # Increase book's available copies
    books[selected_loan.book_id].available_copies += 1
    
    # Save changes
    save_books(books)
    save_loans(loans)

    book_title = books[selected_loan.book_id].title
    print(f"✅ You have returned '{book_title}' successfully!")
