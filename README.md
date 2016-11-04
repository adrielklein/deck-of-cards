[![Build Status](https://travis-ci.org/adrielklein/deck-of-cards.svg?branch=master)](https://travis-ci.org/adrielklein/deck-of-cards)
[![Heroku Status](https://heroku-badge.herokuapp.com/?app=deck-of-cards)](http://deck-of-cards.herokuapp.com)

#Deck of Cards


## :black_joker: Welcome to Deck of Cards :black_joker:
Deck of Cards is a simple web app that allows users to draw from, shuffle, and reset a standing deck of playing carsd.


:black_joker:

`curl -i -X POST -d '{ "suit": "S", "rank": "A" }' http://localhost:5000/card` --> `HTTP/1.0 201 CREATED`
`curl -X PUT localhost:5000/card` --> `{"rank": "A", "suit": "S"}`