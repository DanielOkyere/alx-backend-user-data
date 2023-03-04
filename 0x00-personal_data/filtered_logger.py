#!/usr/bin/env python3
"""0-Regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    for m in fields:
        message = re.sub(f'{m}=.*?{separator}',
                         f'{m}={redaction}{separator}',
                         message)
    return message
