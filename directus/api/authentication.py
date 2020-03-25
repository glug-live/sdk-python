# -*- coding: utf-8 -*-
"""
Directus authentication module containing API calls and types.
"""

from typing_extensions import TypedDict
from directus.base import BaseAPI


class AuthenticateData(TypedDict):
    """
    Authentication payload.
    """

    email: str
    password: str


class RefreshData(TypedDict):
    """
    Refresh payload.
    """

    token: str


class PasswordRequestData(TypedDict):
    """
    Reset password request payload.
    """

    email: str


class PasswordResetData(TypedDict):
    """
    Reset password payload.
    """

    token: str
    password: str


class AuthenticationAPI(BaseAPI):
    """
    # Authentication API

    See https://docs.directus.io/api/authentication.html
    """

    def auth_authenticate(self, data: AuthenticateData):
        """
        See https://docs.directus.io/api/authentication.html#retrieve-a-temporary-access-token
        """
        return self.post("/{project}/auth/authenticate", json=data)

    def auth_refresh(self, data: RefreshData):
        """
        See https://docs.directus.io/api/authentication.html#refresh-a-temporary-access-token
        """
        return self.post("/{project}/auth/refresh", json=data)

    def auth_password_request(self, data: PasswordRequestData):
        """
        See https://docs.directus.io/api/authentication.html#request-a-password-reset
        """
        return self.post("/{project}/auth/password/request", json=data)

    def auth_password_reset(self, data: PasswordResetData):
        """
        See https://docs.directus.io/api/authentication.html#reset-a-password
        """
        return self.post("/{project}/auth/password/reset", json=data)
