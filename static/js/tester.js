/* var testing = "testing11"
    var data = "testing22"

    function initMap() {
      
      var options = { 
        center: { lat: 53.323543, lng: -6.265295},
        zoom: 14,
        mapTypeControl: true,
        mapTypeControlOptions: {
          mapTypeIds: [
            google.maps.MapTypeId.ROADMAP,
            google.maps.MapTypeId.SATELLITE,
          ],
        }
      };


    fetch('/fetch')
        .then(response => response.json())
        .then(data => { 
            fetchFunction(data);
        })
        .catch(err => console.log(err));


    function fetchFunction(data) {
        console.log(data)

    
    for(var i = 0; i < data.length; i++){
        let markerName = data[i].sagaTitle;
        console.log(markerName + "  "+ "testing0000" );
    }
        var markerPlace = {lat: (data[i].lat), lng: (data[i].lng)};
        var marker = new google.maps.Marker({
          position: markerPlace,
          map: map,
        });
        
      var infoWindow = new google.maps.InfoWindow({
        content: data[0].sagaTagline 
      });

      marker.addListener("click", function () {
        infoWindow.open(map, marker);
      });     
    };

   var map = new google.maps.Map(document.getElementById("map"), options);
    }
    
    console.log(testing)
    console.log(data) */