import pytest

from deck import Deck
from main import create_app


@pytest.fixture
def app():
    return create_app(Deck())
