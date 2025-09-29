import pytest
from pathlib import Path

def pytest_configure(config):
    """Configure test environment."""
    pass

@pytest.fixture
def asset_root():
    """Return the root directory of the assets package."""
    return Path(__file__).parent.parent