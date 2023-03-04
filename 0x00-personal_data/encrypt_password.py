#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Expects string password and returns
    salt, hashpassword and byte string"""
    data = bcrypt.hashpw(password.encode(),
                         bcrypt.gensalt())
    return data


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates password"""
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
