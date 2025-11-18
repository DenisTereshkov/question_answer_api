import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    print("Создание тестового клиента...")
    client = TestClient(app)
    return client
