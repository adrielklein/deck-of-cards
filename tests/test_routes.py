import json
from unittest.mock import Mock

from app.deck import Deck
from app.main import create_app


def test_when_acknowledge_route_is_hit_then_it_returns_ok(app):
    with app.test_client() as test_client:
        response = test_client.get('/acknowledge')
        assert 200 == response.status_code
        assert 'OK' == response.get_data().decode()


def test_when_add_card_route_is_hit_then_add_card_to_deck():
    deck = Deck()
    app = create_app(deck)
    with app.test_client() as test_client:
        response = test_client.post('/card', data=b'{ "suit": "S", "rank":"A"}')
        assert 201 == response.status_code
    card = deck.draw()
    assert 'S' == card.suit
    assert 'A' == card.rank


def test_when_draw_card_route_is_hit_then_retrieve_card():
    app = create_app(Deck())
    with app.test_client() as test_client:
        test_client.post('/card', data=b'{ "suit": "S", "rank":"A"}')

        response = test_client.put('/card')
        assert 200 == response.status_code
        response_data = json.loads(response.get_data().decode())
        assert 'S' == response_data['suit']
        assert 'A' == response_data['rank']


def test_when_deck_is_empty_then_get_card_route_return_error():
    app = create_app(Deck())
    with app.test_client() as test_client:
        response = test_client.put('/card')
        assert 400 == response.status_code
        error_message = json.loads(response.get_data().decode())['errorMessage']
        assert 'No cards to draw. Please reset the deck or add cards.' == error_message


def test_shuffle_route():
    shuffle_mock = Mock()
    app = create_app(deck=Mock(shuffle=shuffle_mock))
    with app.test_client() as test_client:
        response = test_client.put('/shuffle')
        assert 200 == response.status_code
    shuffle_mock.assert_called_with()


def test_reset_route():
    reset_mock = Mock()
    app = create_app(deck=Mock(reset=reset_mock))
    with app.test_client() as test_client:
        response = test_client.put('/reset')
        assert 200 == response.status_code
    reset_mock.assert_called_with()


def test_cards_left_route():
    app = create_app(Deck())
    with app.test_client() as test_client:
        response = test_client.get('/numCardsLeft')
        assert 200 == response.status_code
        assert 0 == json.loads(response.get_data().decode())['numCardsLeft']
