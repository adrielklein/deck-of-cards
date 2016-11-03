import pytest

from deck import Deck


def test_when_deck_is_initialized_then_it_is_empty():
    deck = Deck()
    assert 0 == deck.get_num_remaining_cards()


def test_when_cards_are_added_to_the_deck_then_deck_is_not_empty():
    deck = Deck()
    deck.add_card(1)
    assert 1 == deck.get_num_remaining_cards()


def test_when_card_is_added_to_the_deck_and_then_drawn_then_deck_is_empty():
    deck = Deck()
    deck.add_card(1)
    assert 1 == deck.draw()
    assert 0 == deck.get_num_remaining_cards()


def test_when_deck_is_reset_then_remaining_cards_is_reset():
    deck = Deck()
    deck.add_card(1)
    deck.draw()
    deck.reset()
    assert 1 == deck.get_num_remaining_cards()
    assert 0 == deck.get_num_drawn_cards()


def test_when_some_cards_have_been_drawn_and_deck_is_reset_then_deck_is_full_again():
    deck = Deck()
    deck.add_card(1)
    deck.add_card(2)
    deck.draw()
    deck.reset()
    assert 2 == deck.get_num_remaining_cards()
    assert 0 == deck.get_num_drawn_cards()


def test_when_deck_is_empty_and_user_draws_card_then_raise_exception():
    deck = Deck()
    with pytest.raises(Exception) as excinfo:
        deck.draw()
    assert 'No cards to draw. Please reset the deck or add cards.' == str(excinfo.value)


def test_when_deck_is_shuffled_then_cards_get_different_ordering():
    deck = Deck()
    for i in range(100):
        deck.add_card(i)
    deck.shuffle()
    assert [i for i in range(100)] != deck.remaining_cards
