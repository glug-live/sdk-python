# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

from directus.api import ServerAPI, AuthenticationAPI


class Directus(ServerAPI, AuthenticationAPI):
    """
    Provide predefined api calls to the desired Directus API.
    """
