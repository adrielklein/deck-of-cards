import json

from flask import request

from app.card import Card


class AcknowledgeRoute(object):
    path = '/acknowledge'
    endpoint = 'acknowledge'
    method = 'GET'

    def handle(self):
        return 'OK'


class AddCardRoute(object):
    path = '/card'
    endpoint = 'add_card'
    method = 'POST'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        request_info = json.loads(request.get_data().decode())
        suit = request_info['suit']
        rank = request_info['rank']
        card = Card(suit, rank)
        self.deck.add_card(card)
        return '', 201


class DrawCardRoute(object):
    path = '/card'
    endpoint = 'get_card'
    method = 'PUT'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        if 0 == self.deck.get_num_remaining_cards():
            return json.dumps({'errorMessage': 'No cards to draw. Please reset the deck or add cards.'}), 400
        card = self.deck.draw()
        result = {'suit': card.suit, 'rank': card.rank}
        return json.dumps(result)


class DrawCardRoute(object):
    path = '/card'
    endpoint = 'get_card'
    method = 'PUT'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        if 0 == self.deck.get_num_remaining_cards():
            return json.dumps({'errorMessage': 'No cards to draw. Please reset the deck or add cards.'}), 400
        card = self.deck.draw()
        result = {'suit': card.suit, 'rank': card.rank}
        return json.dumps(result)


class ShuffleRoute(object):
    path = '/shuffle'
    endpoint = 'shuffle'
    method = 'PUT'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        self.deck.shuffle()
        return ''


class ResetRoute(object):
    path = '/reset'
    endpoint = 'reset'
    method = 'PUT'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        self.deck.reset()
        return ''


class NumCardsLeftRoute(object):
    path = '/numCardsLeft'
    endpoint = 'num_cards_left'
    method = 'GET'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        result = {'numCardsLeft': self.deck.get_num_remaining_cards()}
        return json.dumps(result)
