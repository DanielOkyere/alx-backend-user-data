#!/usr/bin/env python3
"""Class basic Auth"""

from .auth import Auth
import base64
import re


class BasicAuth(Auth):
    """Basic Auth inherits Auth"""
    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """Extract Base64 authorization"""
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            f_match = re.fullmatch(pattern, authorization_header.strip())
            if f_match is not None:
                return f_match.group('token')
        return None

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """Decodes the value of Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            enc = base64_authorization_header.encode('utf-8')
            dec64 = base64.b64decode(enc)
            decoded = dec64.decode('utf-8')
        except BaseException:
            return None

        return decoded
