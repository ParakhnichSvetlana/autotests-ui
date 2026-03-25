import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    ...

@pytest.fixture(scope="session")
def settings():
    ...