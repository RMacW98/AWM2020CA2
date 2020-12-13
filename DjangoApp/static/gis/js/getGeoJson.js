    var map = L.map('map', {
            center: [53, -6],
            zoom: 5
        }
    );

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar'}).addTo(map);

   var geojsonMarkerOptions = {
        radius: 8,
        fillColor: "#ffffff",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    };

   function onEachFeature(feature, layer) {
        // does this feature have a property named popupContent?
        if (feature.properties && feature.properties.name) {
            layer.bindPopup(feature.properties.name + "<br>" + feature.properties.website);
        }
    }

    L.geoJSON(campsites, {
        onEachFeature: onEachFeature,
        pointToLayer: function (feature, latlng) {
                return L.circleMarker(latlng, geojsonMarkerOptions);
            },
        filter: function(feature, layer) {
                return feature.properties.website;
            }
        }).addTo(map);