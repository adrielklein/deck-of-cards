import json

from flask import request

from card import Card


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


class GetCardRoute(object):
    path = '/card'
    endpoint = 'get_card'
    method = 'GET'

    def __init__(self, deck):
        self.deck = deck

    def handle(self):
        if 0 == self.deck.get_num_remaining_cards():
            return json.dumps({'errorMessage': 'No cards to draw. Please reset the deck or add cards.'}), 400
        card = self.deck.draw()
        result = {'suit': card.suit, 'rank': card.rank}
        return json.dumps(result)
