#!/usr/bin/env python3
"""0-Regex-ing"""
from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """Returns a Logger Object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.SreamHandler()
    stream_handler .setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(),
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
