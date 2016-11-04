[![Build Status](https://travis-ci.org/adrielklein/deck-of-cards.svg?branch=master)](https://travis-ci.org/adrielklein/deck-of-cards)


#:black_joker: Deck of Cards :black_joker:
A simple web app that allows users to draw from, shuffle, and reset a deck of playing cards. The app is deplyed on [Python 3.5](http://deck-of-cards.herokuapp.com)

##Description

When the server starts, the standard 52 playing cards are added to the deck. Users can then draw cards from the deck until it is empty. Once the deck is empty, users may reset the deck to start over.

The deck is not shuffled by default, but users may shuffle it at any time. Users can also check how many cards are left in the deck. Although the deck contains the regular 52 cards, users may also add additional cards.


## Routes
- `POST /card`: Adds a card to the deck
  - `curl -i -X POST -d '{ "suit": "S", "rank": "A" }' http://localhost:5000/card` --> `HTTP/1.0 201 CREATED`
- `PUT /card`: Draws a card from the deck. If the deck is empty then returns an error
  - `curl -X PUT localhost:5000/card` --> `{"rank": "A", "suit": "S"}`
  - `curl -X PUT localhost:5000/card` -->`{"errorMessage": "No cards to draw. Please reset the deck or add cards."}`
- `PUT /shuffle`: Shuffles the cards in the deck
- `PUT /reset`: Puts all the drawn cards back in the deck
- `GET /numCardsLeft`: Gets the number of cards left in the deck
  - `curl -X GET https://deck-of-cards.herokuapp.com/numCardsLeft` --> `{"numCardsLeft": 50}`
  
## Build Instructions
1. Download and install [Python 3.5](https://www.python.org/downloads/release/python-350/)
1. Clone this repository to your machine
1. Open a terminal and change into the root of the repository
1. Install virtualenv `$ pip install virtualenv`
1. Create a virtual environment `$ virtualenv venv`
1. Activate the virtual environment `$ source venv/bin/activate`
1. Install dependencies `$ pip install -r requirements.txt`

## Running the server
- `$ python start_server.py`

## Running the tests
- `$ pytest tests`