from random import shuffle


class Deck(object):
    def __init__(self):
        self.remaining_cards = []
        self.drawn_cards = []

    def add_card(self, card):
        self.remaining_cards.append(card)

    def get_num_remaining_cards(self):
        return len(self.remaining_cards)

    def get_num_drawn_cards(self):
        return len(self.drawn_cards)

    def draw(self):
        if self.get_num_remaining_cards() == 0:
            raise Exception('No cards to draw. Please reset the deck or add cards.')
        card = self.remaining_cards.pop()
        self.drawn_cards.append(card)
        return card

    def reset(self):
        self.remaining_cards += self.drawn_cards
        self.drawn_cards = []

    def shuffle(self):
        shuffle(self.remaining_cards)
