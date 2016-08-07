var twitchUrl = "https://api.twitch.tv/kraken/streams/";
var twitchEnd = "?callback=?";
var channels = [];
var cleanName = [];
var chats = [];
var links = [];
{% for stream in streams %}
   channels.push("{{ stream.channelName }}");
   cleanName.push("{{ stream.cleanName }}" );
   chats.push("{{ stream.chats }}");
   links.push("{{ stream.link }}");
{% endfor %}
alert(channels);