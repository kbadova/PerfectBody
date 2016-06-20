(function() {
		$('dd').filter(':nth-child(n+2)').addClass('hide');
		$('dl').on('click', 'dt', function() {
			$(this)
				.next()
					.slideDown(300)
					.siblings('dd')
						.slideUp(300);	
				google.maps.event.trigger(map, 'resize');

		})
    if(window.oppened_tab.length > 0){
      $("dt."+window.oppened_tab).click();
    }
	})();

function reloadWithGetParam(param){
  var url = window.location.href;    
  if (url.indexOf('?') > -1){
     url += '&'+param;
  }else{
     url += '?'+param;
  }
  window.location.href = url;
}

function success(position) {
    console.log("init2")

  var mapcanvas = $('#map');
  //mapcanvas.id = 'mapcontainer';

  // document.querySelector('article').appendChild(mapcanvas);

  var coords = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  
  var options = {
    zoom: 14,
    center: {lat: 42.705371, lng: 23.304216 },
    mapTypeControl: false,
    navigationControlOptions: {
      style: google.maps.NavigationControlStyle.SMALL
    },
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = window.map;
  var marker = new google.maps.Marker({
      position: coords,
      map: map,
      title:"You are here!"
  });
}


function initAutocomplete() {
  console.log("init")
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 42.705371, lng: 23.304216 },
          zoom: 13,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        });

        var input = document.getElementById('pac-input');
        var searchBox = new google.maps.places.SearchBox(input);
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });

        var markers = [];
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();

          if (places.length == 0) {
            return;
          }
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];
          var bounds = new google.maps.LatLngBounds();
          places.forEach(function(place) {
            var icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25)
            };
            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));

            if (place.geometry.viewport) {
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        });
        window.map = map;
      }

$(document).ready(function() {
      initAutocomplete();
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success);
      } else {
        alert('test')
        error('Geo Location is not supported');
      }

  
  $("dt.history").click(function(){
    reloadWithGetParam("tab=history");
  });

  $("form[name='change_password']").submit(function(e){
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url:'/change_password',
      data:form.serialize(),
      type: "POST",
      success:function(data){        
        console.log(data);
      }
    });
  })

  $("form[name='change_data']").submit(function(e){
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url:'/change_data',
      data:form.serialize(),
      type: "POST",
      success:function(data){        
        console.log(data);
        $("#bmi").html(data['BMI']);
        $("#cal").html(data['max_cal']);
      }
    });
  })

  $("form[name='breakfast']").submit(function(e){
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url:'/breakfast',
      data:form.serialize(),
      type: "POST",
      success:function(data){        
        if(data['success']) {
          fields = data['data'];
          Object.keys(fields).forEach(function(key) {
            var query = ['input[type="checkbox"]', '[value="', key, '"]'].join("");
            $(query)
              .parent('.fields-container')
              .append(['<span> - ', fields[key], '</span> g'].join(""))
          });
        }
      }
    });
  })

  $("form[name='lunch']").submit(function(e){
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url:'/lunch',
      data:form.serialize(),
      type: "POST",
      success:function(data){        
        if(data['success']) {
          fields = data['data'];
          Object.keys(fields).forEach(function(key) {
            var query = ['input[type="checkbox"]', '[value="', key, '"]'].join("");
            $(query)
              .parent('.fields-container')
              .append(['<span> - ', fields[key], '</span> g'].join(""))
          });
        }
      }
    });
  })

  $("form[name='dinner']").submit(function(e){
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url:'/dinner',
      data:form.serialize(),
      type: "POST",
      success:function(data){        
        if(data['success']) {
          fields = data['data'];
          Object.keys(fields).forEach(function(key) {
            var query = ['input[type="checkbox"]', '[value="', key, '"]'].join("");
            $(query)
              .parent('.fields-container')
              .append(['<span> - ', fields[key], '</span> g'].join(""))
          });
        }
      }
    });
  })

  initAutocomplete();

});