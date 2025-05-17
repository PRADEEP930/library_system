# -*- coding: utf-8 -*-
"""
@author: admin
"""
# models.py

from dataclasses import dataclass
from datetime import date

@dataclass
class Book:
    id: str
    title: str
    author: str
    publication_year: int
    total_copies: int
    available_copies: int

@dataclass
class Member:
    id: str
    name: str
    email: str
    password_hash: str
    join_date: date 

@dataclass
class Loan:
    book_id: str
    member_id: str
    issue_date: date
    return_date: date | None = None  # None if not returned yet


