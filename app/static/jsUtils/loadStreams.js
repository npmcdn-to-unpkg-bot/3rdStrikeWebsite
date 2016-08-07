for (var i = 0; i < links.length; i++) {
	
	var mainDiv = document.getElementById("linkHolder");
	var element = document.createElement("button");
	element.innerHTML = cleanName[i];	
	element.id = channels[i];
	element.className = "btn";
	element.style.fontFamily = "Impact";
	element.style.letterSpacing = ".5px";

	$(document).ready(function(streamer){
		$.getJSON(twitchUrl+streamer+twitchEnd, function(data){
			if (data && data.stream) {
				document.getElementById(streamer).style.color = "red";
			}
			else {
				document.getElementById(streamer).style.color = "black";
			}
		});
	}(channels[i]));
	
	
	mainDiv.appendChild(element);
	element.onclick = (function(link, chat) {
		return function() {
			document.getElementById("video").src = link;
			document.getElementById("vidChat").src = chat;
		}
	})(links[i], chats[i]);
}