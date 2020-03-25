# -*- coding: utf-8 -*-
"""
Directus system module containing API calls and types.
"""

from typing_extensions import TypedDict
from directus.base import BaseAPI


class InfoParams(TypedDict):
    """
    Info query params.
    """

    super_admin_token: str


class ServerAPI(BaseAPI):
    """
    # Server API

    See https://docs.directus.io/api/server.html
    """

    def server_info(self, params: InfoParams):
        """
        See https://docs.directus.io/api/server.html#retrieve-server-info
        """
        return self.get("/server/info", params=params)

    def server_ping(self):
        """
        See https://docs.directus.io/api/server.html#ping-the-server
        """
        return self.get("/server/ping")
