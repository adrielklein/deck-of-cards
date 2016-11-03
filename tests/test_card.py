from app.card import Card


def test_when_card_is_created_then_suit_and_rank_are_set():
    card = Card('S', 'A')
    assert 'S' == card.suit
    assert 'A' == card.rank