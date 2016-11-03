import pytest

from app.deck import Deck
from app.main import create_app


@pytest.fixture
def app():
    return create_app(Deck())
