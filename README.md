
# Project 2 – 📚 *Library Management System*

### 1. Learning Goals

- Design a **mini-database** with CSV files
- Model **many-to-many** (members ↔ loans)
- Practise **login, roles, password hashing**
- Implement **CRUD** operations & due-date logic

### 2. System Roles
Role
Permissions
Librarian
add / delete books, register members, issue/return, view overdue
Member
search catalogue, check availability, see own loan history

### 3. File Schema

| File | Columns | Example Line |
| --- | --- | --- |
| `books.csv` | ISBN,Title,Author,CopiesTotal,CopiesAvailable | `9780132350884,Clean Code,Robert C. Martin,5,3` |
| `members.csv` | MemberID,Name,**PasswordHash**,Email,JoinDate | `1001,Ananya Singh,$2b$12$...Q3,ananya@mail.com,2025-05-10` |
| `loans.csv` | LoanID,MemberID,ISBN,IssueDate,DueDate,ReturnDate | `42,1001,9780132350884,2025-05-15,2025-05-29,` |

> 🔐 Hash passwords with bcrypt (pip install bcrypt).

### 4. Step-by-Step Build Plan
Phase
Tasks
4.1 Setup
models.py (Book, Member, Loan dataclasses) & storage.py (CSV read/write helpers).
4.2 Auth
auth.py with register_member() & login(role). Store logged-in user in session dict.
4.3 Librarian Menu
1) Add book 2) Remove book 3) Issue book 4) Return book 5) View overdue list 6) Logout.
4.4 Member Menu
1) Search catalogue (title / author keyword) 2) Borrow book (if available) 3) My loans 4) Logout.
4.5 Business Rules
Issue: decrement CopiesAvailable, create loan, due = issue+14d.  Return: fill ReturnDate, increment copies.
4.6 Overdue Report
Select loans where ReturnDate='' and DueDate < today; pretty-print table, e-mail reminder optional.
4.7 Validation & Errors
- Invalid ISBN - Duplicate member IDs - Negative copies - Password mismatch.
4.8 Tests
pytest tests/test_issue_return.py (issue then return restores availability).
4.9 Argparse
--data-dir ./data flag to load CSVs from custom folder.

### 5. Console Snapshot
=== Librarian Dashboard ===
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Overdue List
6. Logout
> 3
ISBN to issue: 9780132350884
Member ID: 1001
✔ Book issued. Due on 29-May-2025.
