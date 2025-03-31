import pytest
from fastapi.testclient import TestClient

from cvtracker.app import app


@pytest.fixture
def test_client():
    client = TestClient(app)
    return client
