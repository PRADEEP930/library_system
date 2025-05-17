# -*- coding: utf-8 -*-
"""
@author: admin
"""

# storage.py

import csv
from datetime import datetime
from models import Book, Member, Loan

BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"
LOANS_FILE = "loans.csv"

# === BOOK STORAGE ===

def load_books():
    books = {}
    try:
        with open(BOOKS_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                books[row['ISBN']] = Book(
                    id=row['ISBN'],
                    title=row['Title'],
                    author=row['Author'],
                    publication_year=row.get('PublicationYear'),
                    total_copies=int(row['CopiesTotal']),
                    available_copies=int(row['CopiesAvailable'])
                )
    except FileNotFoundError:
        pass
    return books

def save_books(books: dict[str, Book]):
    with open(BOOKS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ISBN', 'Title','publication_year', 'Author', 'CopiesTotal', 'CopiesAvailable'])
        writer.writeheader()
        for book in books.values():
            writer.writerow({
                'ISBN': book.id,
                'Title': book.title,
                'Author': book.author,
                'publication_year':book.publication_year,
                'CopiesTotal': book.total_copies,
                'CopiesAvailable': book.available_copies
            })

# === MEMBER STORAGE ===

def load_members():
    members = {}
    try:
        with open(MEMBERS_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                members[row['MemberID']] = Member(
                    id=row['MemberID'],
                    name=row['Name'],
                    email=row['Email'],
                    password_hash=row['PasswordHash'],
                    join_date=datetime.strptime(row['JoinDate'], "%Y-%m-%d").date(),
                )
    except FileNotFoundError:
        pass
    return members

def save_members(members: dict[str, Member]):
    with open(MEMBERS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['MemberID', 'Name', 'Email', 'PasswordHash', 'JoinDate'])
        writer.writeheader()
        for member in members.values():
            writer.writerow({
                'MemberID': member.id,
                'Name': member.name,
                'Email': member.email,
                'PasswordHash': member.password_hash,  # Will be added later in auth.py
                'JoinDate': member.join_date
            })

# === LOAN STORAGE ===

def load_loans():
    loans = []
    try:
        with open(BOOKS_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                loans.append(Loan(
                    book_id=row['ISBN'],
                    member_id=row['MemberID'],
                    issue_date=datetime.strptime(row['IssueDate'], '%Y-%m-%d').date(),
                    return_date=datetime.strptime(row['ReturnDate'], '%Y-%m-%d').date() if row['ReturnDate'] else None
                ))
    except FileNotFoundError:
        pass
    return loans

def save_loans(loans: list[Loan]):
    with open(LOANS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
        writer.writeheader()
        for idx, loan in enumerate(loans, start=1):
            writer.writerow({
                'LoanID': idx,
                'MemberID': loan.member_id,
                'ISBN': loan.book_id,
                'IssueDate': loan.issue_date.strftime('%Y-%m-%d'),
                'DueDate': (loan.issue_date.replace(day=loan.issue_date.day+14)).strftime('%Y-%m-%d'),  # Fixed period
                'ReturnDate': loan.return_date.strftime('%Y-%m-%d') if loan.return_date else ''
            })
