# -*- coding: utf-8 -*-

from json import loads
from directus import Directus


def test_authentication_authenticate(client: Directus):
    body = {"email": "admin@example.com", "password": "password"}
    res = client.auth_authenticate(data=body)
    assert loads(res.request.body) == body
    assert res.status_code == 200
