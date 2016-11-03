
#Deck of Cards

`curl -i -X POST -d '{ "suit": "S", "rank": "A" }' http://localhost:5000/card` --> `HTTP/1.0 201 CREATED`
`curl -X PUT localhost:5000/card` --> `{"rank": "A", "suit": "S"}`