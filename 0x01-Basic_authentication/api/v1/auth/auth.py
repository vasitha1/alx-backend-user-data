#!/usr/bin/env python3
"""
Authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine whether a given path requires authentication.
        Currently, returns False (no auth required).
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return the authorization header from the request.
        Currently, returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return the current user based on the request.
        Currently, returns None.
        """
        return None
