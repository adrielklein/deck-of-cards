import json
from unittest.mock import Mock

from flask import Flask

from start_server import start_server

SUITS = ['S', 'H', 'D', 'C']
RANKS = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']


def test_when_user_starts_server_then_app_starts_serving(monkeypatch):
    mocked_run = Mock()
    monkeypatch.setattr(Flask, 'run', mocked_run)
    start_server()
    mocked_run.assert_called_with(host='0.0.0.0', port=5000)


def test_when_user_starts_server_then_standard_52_cards_are_added_to_deck(monkeypatch):
    mocked_run = Mock()
    monkeypatch.setattr(Flask, 'run', mocked_run)
    app = start_server()
    with app.test_client() as test_client:
        response = test_client.get('/numCardsLeft')
        assert 52 == json.loads(response.get_data().decode())['numCardsLeft']
        for i in range(52):
            response = json.loads(test_client.put('/card').get_data().decode())
            assert response['suit'] in SUITS
            assert response['rank'] in RANKS
