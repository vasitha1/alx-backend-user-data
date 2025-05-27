#!/usr/bin/env python3
"""
Authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine whether a given path requires authentication.
        Currently, returns False (no auth required).
        """
        return False

    def authorization_header(self, request=None) -> None:
        """
        Return the authorization header from the request.
        Currently, returns None.
        """
        return None

    def current_user(self, request=None) -> None:
        """
        Return the current user based on the request.
        Currently, returns None.
        """
        return None


if __name__ == "__main__":
    a = Auth()

    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())
