# -*- coding: utf-8 -*-

from typing_extensions import TypedDict
from directus.base import BaseAPI


class AuthenticateData(TypedDict):
    email: str
    password: str


class RefreshData(TypedDict):
    token: str


class ResetPasswordRequestData(TypedDict):
    email: str


class ResetPasswordData(TypedDict):
    token: str
    password: str


class AuthenticationAPI(BaseAPI):
    """
    # Authentication API

    See https://docs.directus.io/api/authentication.html
    """

    def authenticate(self, data: AuthenticateData):
        """
        See https://docs.directus.io/api/authentication.html#retrieve-a-temporary-access-token
        """
        return self.post("/{project}/auth/authenticate", json=data)

    def auth_refresh(self, data: RefreshData):
        """
        See https://docs.directus.io/api/authentication.html#refresh-a-temporary-access-token
        """
        return self.post("/{project}/auth/refresh", json=data)

    def auth_password_reset_request(self, data: ResetPasswordRequestData):
        """
        See https://docs.directus.io/api/authentication.html#request-a-password-reset
        """
        return self.post("/{project}/auth/password/request", json=data)

    def auth_password_reset(self, data: ResetPasswordData):
        """
        See https://docs.directus.io/api/authentication.html#reset-a-password
        """
        return self.post("/{project}/auth/password/reset", json=data)
