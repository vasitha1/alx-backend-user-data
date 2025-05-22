#!/usr/bin/env python3
"""
Module providing a utility function to redact sensitive data from log messages.
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Replaces values of specified fields in log message with a redaction string.
    """
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1={}'.format(redaction), message)
