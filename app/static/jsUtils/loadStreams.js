for (var i = 0; i < links.length; i++) {
	
	var mainDiv = document.getElementById("linkHolder");
	var element = document.createElement("button");
	element.innerHTML = cleanName[i];	
	element.id = channels[i];
	element.className = "btn";
	element.style.fontWeight = "bold";
	element.style.letterSpacing = ".5px";
	element.style.borderRadius = "15px 50px 30px";

	$(document).ready(function(streamer, link, chatLink){
		$.getJSON(twitchUrl+streamer+twitchEnd, function(data){
			if (data && data.stream) {
				document.getElementById('video').src=link;
				document.getElementById('vidChat').src=chatLink;
				document.getElementById(streamer).style.color = "red";
			}
		});
	}(channels[i], link=links[i], chatLink=chats[i]));
	
	mainDiv.appendChild(element);

	element.onclick = (function(link, chat, channelID) {
		return function() {
			// Update video and chat divs
			var channel = document.getElementById(channelID);
			var videoDiv = document.getElementById("video");
			var chatWindow = document.getElementById("vidChat");
			if (videoDiv.src != link) {
				// return other ids to black
				for (var i = 0; i < channels.length; i++) {
					i = i.toString();
					if (document.getElementById(channels[i]).style.color != 'red'){ 
						document.getElementById(channels[i]).style.color = "black";
					}
				}
				channel.style.color = "blue";
			}
			videoDiv.src = link;
			chatWindow.src = chat;
		}
	})(links[i], chats[i], channels[i]);
}