# -*- coding: utf-8 -*-

from json import loads
from directus import Directus


def test_authentication_authenticate(client: Directus):
    body = {"email": "admin@example.com", "password": "password"}
    res = client.authenticate(data=body)
    assert loads(res.request.body) == body
    print(res.content)
    assert res.status_code == 201
