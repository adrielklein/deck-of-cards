from app.card import Card
from app.deck import Deck
from app.main import create_app

SUITS = ['S', 'H', 'D', 'C']
RANKS = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']


def create_deck():
    deck = Deck()
    for suit in SUITS:
        for rank in RANKS:
            deck.add_card(Card(suit, rank))
    return deck


def start_server():
    app = create_app(create_deck())
    app.run(host='0.0.0.0', port=5000)
    return app


if __name__ == '__main__':
    start_server()
