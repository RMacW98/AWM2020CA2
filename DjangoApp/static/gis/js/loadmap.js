var HOST = location.protocol + "//" + location.host;
var locationMarker;
var circle;


var map = L.map('map', {
    center: [53, -6],
        zoom: 5
}
);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar'}).addTo(map);
updateLocation(map);
map.on('touchstart click dblclick ', function () {
        updateLocation(map);
});

function updateLocation(map) {
       navigator.geolocation.getCurrentPosition(function (pos) {
           setMapToCurrentLocation(map, pos);
           update_db(pos);
           },
           function (err) {},
           {enableHighAccuracy: true,timeout: 30000
           });
}

function setMapToCurrentLocation(map, pos) {
    console.log("In setMapToCurrentLocation.");
    var myLatLon = L.latLng(pos.coords.latitude, pos.coords.longitude);
    map.flyTo(myLatLon, 16);if (locationMarker) {
        map.removeLayer(locationMarker);
    }
    //var icon = L.icon({iconUrl: 'data/blue.png'});
    locationMarker = L.marker(myLatLon).addTo(map);
    $(".toast+body").html("Found location<br>Lat: " + myLatLon.lat + " Lon: " + myLatLon.lng);
    $(".toast").toast('show');
}


function update_db(pos) {
    var locString = pos.coords.longitude + ", " + pos.coords.latitude;
    $.ajax({
        type: "POST",
        headers: {
            'X-CSRFToken' : getCookie('csrftoken')
        },
        url: HOST + "/world/updatedb/",
        data: {
            point: locString
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

