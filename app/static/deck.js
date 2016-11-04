function setNumCardsLeft(){
    $.ajax({
        url: '/numCardsLeft',
        type: 'GET',
        success: function(result) {
            result = JSON.parse(result);
            $("#numCardsLeft").text("Number of cards left: " + result['numCardsLeft'])
        }
    });
}

SUIT_LETTER_2_NAME = {C: "clubs", S: "spades", D: "diamonds", H: "hearts"}

function draw(){
    $.ajax({
        url: '/card',
        type: 'PUT',
        success: function(result) {
            result = JSON.parse(result);
            $("#drawnCard").text("You drew a " + result["rank"]+ " of " + SUIT_LETTER_2_NAME[result['suit']]);
        },
        error: function(result){
            result = JSON.parse(result['responseText']);
            $("#drawnCard").text(result['errorMessage']);
        }
    });
    setNumCardsLeft();
}

function reset(){
    $.ajax({
        url: '/reset',
        type: 'PUT',
        success: function(result) { }
    });
    setNumCardsLeft();
}

function shuffle(){
    $.ajax({
        url: '/shuffle',
        type: 'PUT',
        success: function(result) { }
    });
    setNumCardsLeft();
}
