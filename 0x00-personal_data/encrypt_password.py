#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Expects string password and returns
    salt, hashpassword and byte string"""
    data = bcrypt.hashpw(password.encode(),
                         bcrypt.gensalt())
    return data
