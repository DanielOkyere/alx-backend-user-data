#!/usr/bin/env python3
"""Empty Session"""
from auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session Auth that inherits Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session Id"""
        if not isinstance(user_id, str)\
           or user_id is None:
            return None
        new_key = str(uuid4())
        self. user_id_by_session_id[new_key] = user_id
        return new_key
