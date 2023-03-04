#!/usr/bin/env python3
"""0-Regex-ing"""
from typing import List
import re
import logging
from os import environ
import mysql.connector

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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to secure database"""
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    cnx = mysql.connector.connection.MySQLConnection(user=username,
                                                     password=password,
                                                     host=host,
                                                     database=db_name)
    return cnx


def main():
    """Obtain database connection"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')
    field_name = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_name))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


def get_logger() -> logging.Logger:
    """Returns a Logger Object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
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


if __name__ == '__main__':
    main()
