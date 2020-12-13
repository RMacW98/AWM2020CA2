var actual = '{{ clinics | safe }}';
console.log(actual);

var actuals = JSON.parse(actual)

document.write("<div id=\"campsite\">" +
                "<h1>Nearby Clinics</h1>");

            for (var i = 0; i < actuals.length; i++){
                document.write("<ul class=\"list-group list-group-flush\">" +
                        "<li class=\"list-group-item d-flex justify-content-between align-items-center\">"
                         + actuals[i].fields.name +
                        "<br></li></ul>");

                L.marker([actuals[i].fields.lat, actuals[i].fields.lon]).addTo(map).bindPopup("Name:" + actuals[i].fields.name);
            }

            document.write("</div>");