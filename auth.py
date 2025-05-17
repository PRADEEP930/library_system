# -*- coding: utf-8 -*-
"""
@author: admin
"""

# auth.py

import bcrypt
from datetime import datetime
from models import Member
from storage import load_members, save_members

# === PASSWORD UTILS ===

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# === USER AUTH ===

def register_user():
    members = load_members()
    member_id = input("Enter Member ID: ")
    if member_id in members:
        print("Member ID already exists!")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    hashed = hash_password(password)
    join_date = datetime.today().strftime('%Y-%m-%d')

    new_member = Member(
        id=member_id,
        name=name,
        email=email,
        password_hash=hashed,
        join_date=join_date
    )

    members[member_id] = new_member
    save_members(members)
    print("Registration successful!")

def login_user():
    members = load_members()
    member_id = input("Enter Member ID: ")
    password = input("Enter Password: ")

    member = members.get(member_id)
    if not member:
        print("Member not found!")
        return None

    if not check_password(password, member.password_hash):
        print("Incorrect password!")
        return None

    print(f"Welcome back, {member.name}!")
    return member
