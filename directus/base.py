# -*- coding: utf-8 -*-
"""
Base module contains tools wrapped around the requests Session object.
"""

from urllib.parse import urljoin
from typing import Optional
from abc import ABCMeta

import requests


class BaseAPI(metaclass=ABCMeta):
    """
    Base API provides a basic wrapper around requests.Session, and is used
    to perfom calls against a directus API.
    """

    _session: Optional[requests.Session] = None

    url: str
    project: str

    email: Optional[str]
    password: Optional[str]

    def __init__(
        self,
        url: str,
        project: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.url = url
        self.project = project
        self.email = email
        self.password = password

    @property
    def session(self) -> requests.Session:
        """
        Get the client requests session.
        """
        if self._session is None:
            self._session = requests.Session()
        return self._session

    def _enpoint_url(self, endpoint: str):
        """
        Join base url, with an endpoint.
        """
        return urljoin(self.url, endpoint.format(project=self.project))

    def get(self, url, **kwargs):
        """
        Perfom a GET request on the Directus API.
        """
        return self.session.get(self._enpoint_url(url), **kwargs)

    def post(self, url, **kwargs):
        """
        Perfom a POST request on the Directus API.
        """
        return self.session.post(self._enpoint_url(url), **kwargs)
