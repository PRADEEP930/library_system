# -*- coding: utf-8 -*-
"""
@author: admin
"""

# app.py

from auth import register_member, login
from books import add_book, view_books
from loans import borrow_book, return_book, view_loans

def main_menu():
    while True:
        print("\n=== Library System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register_member()
        elif choice == '2':
            member = login()
            if member:
                user_menu(member)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def user_menu(member):
    while True:
        print(f"\n--- Welcome, {member.name} ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View My Loans")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            borrow_book(member.id)
        elif choice == '4':
            return_book(member.id)
        elif choice == '5':
            view_loans(member.id)
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main_menu()
