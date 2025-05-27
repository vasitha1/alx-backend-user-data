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
        Return True if authentication is required for the given path.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        # Normalize path: remove trailing slash
        normalized_path = path.rstrip('/')

        for exclude in excluded_paths:
            # Normalize excluded path: remove trailing slash
            normalized_exclude = exclude.rstrip('/')
            if normalized_path == normalized_exclude:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

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
