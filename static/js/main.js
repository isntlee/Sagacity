
    function initMap() {
      var options = {
        center: { lat: 53.27249, lng: -6.24206 },
        zoom: 10,
        mapTypeControl: true,
        mapTypeControlOptions: {
          mapTypeIds: [
            google.maps.MapTypeId.ROADMAP,
            google.maps.MapTypeId.SATELLITE,
          ],
        },
      };

      var map = new google.maps.Map(document.getElementById("map"), options);

      var marker = new google.maps.Marker({
        position: { lat: 53.273, lng: -6.243 },
        map: map,
      });

      var infoWindow = new google.maps.InfoWindow({
        content: "<h5>Where are we?</h5>",
      });

      marker.addListener("mouseover", function () {
        infoWindow.open(map, marker);
      });
    }