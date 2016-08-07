function loadMap() {
	var map = L.map('mapid').setView([40, -92], 3, {reset: true});

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    continuousWorld: true,
    id: 'qholness.12608ddf',
    accessToken: 'sk.eyJ1IjoicWhvbG5lc3MiLCJhIjoiY2lyam5zeGdjMDAxb2ZmbTZiYjZpc3hhMiJ9.4SOq99wiolUI23JBUGhyJw'
	}).addTo(map);
	map.scrollWheelZoom.enable();
	return map
}

var Icon = L.icon({
	iconUrl: '/static/images/marker-icon.png',
	iconSize: [15, 20],
    iconAnchor: [10, 20],
    popupAnchor: [-3, -20],
});
// function getColor(d) {
//     return d > 1000 ? '#800026' :
//            d > 500  ? '#BD0026' :
//            d > 200  ? '#E31A1C' :
//            d > 100  ? '#FC4E2A' :
//            d > 50   ? '#FD8D3C' :
//            d > 20   ? '#FEB24C' :
//            d > 10   ? '#FED976' :
//                       '#FFEDA0';
// 	}
// 	function style(feature) {
//     return {
//         fillColor: getColor(feature.properties.density),
//         weight: 2,
//         opacity: 1,
//         color: 'white',
//         dashArray: '3',
//         fillOpacity: 0.7
//     };
// 	}