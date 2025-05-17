# -*- coding: utf-8 -*-
"""
@author: Pradeep Y Yadav
"""

# main.py

from auth import register_user, login_user
from books import add_book,list_books
from loans import borrow_book, return_book

def user_menu(user_email):
    while True:
        print("\n📚 Welcome to the Library System!")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            borrow_book(user_email)
        elif choice == '3':
            return_book(user_email)
        elif choice == '4':
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def admin_menu():
    while True:
        print("\n🛠 Admin Panel:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Exit Admin Panel")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            print("✅ Exiting Admin Panel.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def main():
    print("📖 Welcome to the Simple Library App!")
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Admin Mode")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user_email = login_user()
            if user_email:
                user_menu(user_email)
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("👋 Exiting application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main()
