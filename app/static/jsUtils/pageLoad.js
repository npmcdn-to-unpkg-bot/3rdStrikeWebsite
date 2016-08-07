/*
		Write rankings to document.
		Cans reorder the players table to change rankings.
*/
var players = ["Adam H",
				"Jose DLC", 
				"Quentin H", 
				"Will \"Big Red\"", 
				"Kerry C.", 
				"Mighty Mar",
				"Jose M.",
				"Stephen A.",
				"Miguel S.",
				"Tony V.",
				"Germaine W.",
				];
var rankings = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eigth", "Ninth", "Tenth", "Eleventh", "Twelveth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", "Nineteenth", "Twenty", "TwentyOne", "TwentyTwo", "TwentyThree", "TwentyFour", "TwentyFive", "TwentySix", "TwentySeven", "TwentyEight", "TwentyNine", "Thirty", "ThirtyOne", "ThirtyTwo", "ThirtyThree", ]; 
for (i = 0; i < rankings.length; i++) {
	if(document.getElementById(rankings[i])) {
		if (players[i]) {
			document.getElementById(rankings[i]).innerHTML = players[i];
		}
		else {
			document.getElementById(rankings[i]).innerHTML = i;
		}
	}
}

generateChallengeList(players);