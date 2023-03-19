#!/usr/bin/env python3
"""User Database Table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declartive_base


Base = declarative_base()


class User(Base):
    """Representation of the user table"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
