// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow;

function success(pos) {
  var crd = pos.coords;
  console.log('Sua posição atual é:');
  console.log('Latitude : ' + crd.latitude);
  console.log('Longitude: ' + crd.longitude);
  console.log('Mais ou menos ' + crd.accuracy + ' metros.');
  document.getElementById("flatitude").value = crd.latitude;
  document.getElementById("flongitude").value = crd.longitude;
  document.getElementById("faccuracy").value = crd.accuracy;

};
var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

function success(pos) {
  var crd = pos.coords;
  console.log('Sua posição atual é:');
  //Session com Localização
  localStorage.setItem('latitude',crd.latitude);
  localStorage.setItem('longitude',crd.longitude);
  localStorage.setItem('accuracy',crd.accuracy);
  console.log('Latitude : ' + crd.latitude);
  console.log('Longitude: ' + crd.longitude);
  console.log('Mais ou menos ' + crd.accuracy + ' metros.');
  document.getElementById("flatitude").value = crd.latitude;
  document.getElementById("flongitude").value = crd.longitude;
  document.getElementById("faccuracy").value = crd.accuracy;
};

function error(err) {
  console.warn('ERROR(' + err.code + '): ' + err.message);
};

if ('geolocation' in navigator) {
  navigator.geolocation.getCurrentPosition(success, error, options);

  navigator.geolocation.getCurrentPosition(function(position) {
      console.log(position)
      var geoPosition = position;
      console.log(geoPosition)
  }, function(error) {
      console.log(error)
  })
} else {
  alert('Não foi possivel pegar a Localização')
}

function initMap() {
    //alert("Latitude: " + localStorage.getItem('latitude'));
    var latitude = parseInt(localStorage.getItem('latitude'));
    var longitude = parseInt(localStorage.getItem('longitude'));
    var accuracy  = parseInt(localStorage.getItem('accuracy'));
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: longitude,
      lng: longitude },
      zoom: 20
    });

    infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  locationButton.textContent = "Pan to Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
            accuracy: position.accuracy
          };

          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);
          map.setCenter(pos);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

//navigator.geolocation.getCurrentPosition(success, error, options);