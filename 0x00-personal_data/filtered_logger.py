#!/usr/bin/env python3
"""0-Regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    filter-datum: returns log message obfuscated
    Args:
        fields (List): list of strings representing all fields
        redaction (str): string representing field that will be
            obfuscated
        message (str): string representing the log line
        separator: string representing character to separate fields
    Returns:
        Log message obfuscated
    """
    for m in fields:
        message = re.sub(f'{m}=.*?{separator}',
                         f'{m}={redaction}{separator}',
                         message)
    return message
