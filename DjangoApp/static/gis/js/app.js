// default map layer
let map = L.map('map', {
    layers: MQ.mapLayer(),
    center: [53.2837, -6.3244],
    zoom: 12
});


    function runDirection(start, end) {

        // recreating new map layer after removal
        map = L.map('map', {
            layers: MQ.mapLayer(),
            center: [53.2837, -6.3244],
            zoom: 12
        });

        var dir = MQ.routing.directions();

        dir.route({
            locations: [
                start,
                end
            ]
        });


        CustomRouteLayer = MQ.Routing.RouteLayer;

        map.addLayer(new CustomRouteLayer({
            directions: dir,
            fitBounds: true
        }));
    }

// function that runs when form submitted
function submitForm(event) {
    event.preventDefault();

    // delete current map layer
    map.remove();

    // getting form data
    start = document.getElementById("start").value;
    end = document.getElementById("destination").value;


    runDirection(start, end);


    // reset form
    document.getElementById("form").reset();
}

// asign the form to form variable
const form = document.getElementById('form');

// call the submitForm() function when submitting the form
form.addEventListener('submit', submitForm);
