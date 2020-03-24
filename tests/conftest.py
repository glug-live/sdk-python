# -*- coding: utf-8 -*-

import pytest

from directus import Directus


@pytest.fixture
def client() -> Directus:
    yield Directus("http://localhost:8080", "_", "admin@example.com", "password")
