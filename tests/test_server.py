# -*- coding: utf-8 -*-

from directus import Directus


def test_server_info(client: Directus):
    res = client.server_info(params={"super_admin_token": "token"})
    assert res.status_code == 200


def test_server_ping(client: Directus):
    res = client.server_ping()
    assert res.status_code == 200
    assert res.content == b"pong"
