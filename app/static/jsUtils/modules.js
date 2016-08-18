function generateChallengeList(players) {
	list = document.getElementById("rivalSelector");
	for (i = 0; i < players.length; i++) {
		option = document.createElement("option");
		option.text = players[i];
		option.id = i;
		list.add(option);
		
	}
}

function promptFighters(challenged) {
	// var div = document.createElement("div");
	// div.style.width = "100px";
	// div.style.height = "100px";
	obj = document.getElementById("FightCard1");
	// obj.id = "FightCard";
	obj.innerHTML = "You vs. " + challenged;
	obj.style.letterSpacing = "1px";
}