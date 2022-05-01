let dataset;
let datasetindexpage;
let isInitMap = true;
//alert(12)

var map = L.map('map');//.setView([6.9702465, -75.6507133], 5);


function loadMap() {
  map.setView([2.4702465, -71.2507133], 5.42);
  // var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
  //     maxZoom: 20,
  //     attribution: '',
  //     id: 'mapbox/streets-v11',
  //     tileSize: 512,
  //     zoomOffset: -1
  // }).addTo(map);

  var capaRelieve = new L.tileLayer('http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg');
  var capaOSM = new L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png');

  capaOSM.addTo(map);
  capaRelieve.addTo(map);

  var capasBase = {
    "OpenStreetMap": capaOSM,
    "Relieve": capaRelieve
  };

  if (isInitMap) {
    var selectorCapas = new L.control.layers(capasBase);
    selectorCapas.addTo(map);
  }
}

function onEachFeature(feature, layer) {
  layer.bindTooltip(feature.properties.title).on('click', onClick);
  if (!isInitMap) {
    map.setView([feature.properties.latitude, feature.properties.longitude], 10);
  }
}

function onClick(e) {

  console.log(e);
  const item = e.target.feature.properties;
  let nodeText = '<div class="image-container">';
  if (item.link_video != null && item.link_video != "") {
    console.log(item.link_video)
    nodeText += '<iframe src="' + item.link_video + '" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div> ';
  } else {
    console.log(item.image_data)
    nodeText += '<img src="' + item.image_data.url + '" class="image-item" />';
  }
  nodeText += '</div>'
  nodeText += '<div class="title-detail">' +
    '<h2 class="title">' + item.title + '</h2>' +
    '</div>' +
    '<div class="details-container">' +
    '<p class="description">' + item.intro +
    '</p>' +
    '<div class="stadistics-content">' +
    '<div class="stadistic-item">' +
    '<h3 class="title">Proyectos</h3>' +
    '<img src="/static/images/energia/CierreBrechas_EnergyProyectos.svg" class="image" />' +
    '<label class="number">240</label>' +
    '</div>' +
    '<div class="divider"></div>' +
    '<div class="stadistic-item">' +
    '<h3 class="title">Usuarios</h3>' +
    '<img src="/static/images/energia/CierreBrechas_Usuarios.svg" class="image" />' +
    '<label class="number">' + item.users + '</label>' +
    '</div>' +
    '</div>' +
    '</div>';

  var events = document.getElementById("left-panel");
  events.innerHTML = nodeText;

  var events1 = document.getElementById("titleMobile");
  events1.innerHTML = item.title;

  var events2 = document.getElementById("descriptionMobile");
  events2.innerHTML = item.intro;
}


/* get dataset */
getDataSet = () => {

  loadMap();
  var total_count = 0;
  fetch(`/api/v2/pages/?type=${page}&fields=*`)
    .then((res) => res.json())
    .then(function (data) {
      total_count = data.meta.total_count;
      fetch(`/api/v2/pages/?type=${page}&fields=*&limit=${total_count}`)
        .then((res) => res.json())
        .then(function (data) {
          /* data for markers in map */
          dataset = data;
          /* data for markers in map */
          console.log(dataset);

          let featuresData = [];
          dataset.items.forEach(function (element, indice, array) {
            featuresData.push({
              "type": "Feature",
              "properties": element,
              "geometry":
              {
                "type": "Point",
                "coordinates": [element.longitude, element.latitude]
              }
            });
          });

          let dataLayer =
          {
            "type": "FeatureCollection",
            "features": featuresData
          };

          var markers = L.markerClusterGroup({ showCoverageOnHover: false });

          var geoJsonLayer = L.geoJSON(dataLayer, {

            filter: function (feature, layer) {
              if (feature.properties) {
                // If the property "underConstruction" exists and is true, return false (don't render features under construction)
                return feature.properties.underConstruction !== undefined ? !feature.properties.underConstruction : true;
              }
              return false;
            },

            pointToLayer: function (feature, latlng) {

              let energyTempIcon = L.icon({
                iconUrl: feature.properties.icon.url,
                iconSize: [30, 42],
                iconAnchor: [16, 37],
                popupAnchor: [0, -28]
              });
              return L.marker(latlng, { icon: energyTempIcon });
            },

            onEachFeature: onEachFeature
          });

          markers.addLayer(geoJsonLayer);
          map.addLayer(markers);
          map.fitBounds(markers.getBounds());

          isInitMap = false;
          document.getElementById("loading").style.display = "none";

        })
        .catch((err) => console.error(err));
    })
    .catch((err) => console.error(err));
};

getDataSetIndexPage = () => {
  fetch(`/api/v2/pages/?type=${index}&fields=*`)
    .then((res) => res.json())
    .then(function (data) {
      /* data for landing page  */
      datasetindexpage = data;
      /* data for landing page  */
      console.log(datasetindexpage);
      if (!datasetindexpage || !Array.isArray(datasetindexpage.items) || (datasetindexpage.items == 0)) {
        return;
      }
      var obj = datasetindexpage.items[0];
      if (obj.link_video) {
        console.log('ISDMFISADM')
        document.querySelector('#left-panel #imageItem').outerHTML = `<iframe src="${obj.link_video}"></iframe>`
      }
      document.querySelector('#imageItem')
      document.querySelector('#left-panel #title').innerHTML = obj.title
      document.querySelector('#left-panel #description').innerHTML = obj.intro
      document.querySelector('#left-panel #numProjects').innerHTML = obj.projects
      document.querySelector('#left-panel #numUsers').innerHTML = obj.users      
      document.querySelector('#titleMobile').innerHTML = obj.title;
      document.querySelector('#descriptionMobile').innerHTML = obj.intro;
    })
    .catch((err) => console.error(err));
};
/* get dataset */

document.addEventListener("DOMContentLoaded", function () {

  getDataSet();
  getDataSetIndexPage();
  /* your code here */
});


function searchDepartament(e) {
  map.eachLayer(function (layer) {
    map.removeLayer(layer);
  });

  loadMap(); //reload the map function

  let featuresData = [];
  dataset.items.forEach(function (element, indice, array) {

    if (document.getElementById('search').value === '') {
      isInitMap = true;
      //([feature.properties.latitude, feature.properties.longitude], 10);
    }
    let expression = document.getElementById('search').value.toLowerCase() + '.*';
    if (element.department.toLowerCase().match(new RegExp(expression))) {
      featuresData.push({
        "type": "Feature",
        "properties": element,
        "geometry":
        {
          "type": "Point",
          "coordinates": [element.longitude, element.latitude]
        }
      });
    };

  });

  let dataLayer =
  {
    "type": "FeatureCollection",
    "features": featuresData
  };

  var markers = L.markerClusterGroup({ showCoverageOnHover: false });

  var geoJsonLayer = L.geoJSON(dataLayer, {

    filter: function (feature, layer) {
      if (feature.properties) {
        // If the property "underConstruction" exists and is true, return false (don't render features under construction)
        return feature.properties.underConstruction !== undefined ? !feature.properties.underConstruction : true;
      }
      return false;
    },

    pointToLayer: function (feature, latlng) {

      let energyTempIcon = L.icon({
        iconUrl: feature.properties.icon.url,
        iconSize: [30, 42],
        iconAnchor: [16, 37],
        popupAnchor: [0, -28]
      });
      return L.marker(latlng, { icon: energyTempIcon });
    },

    onEachFeature: onEachFeature
  });

  markers.addLayer(geoJsonLayer);
  map.addLayer(markers);
  map.fitBounds(markers.getBounds());

  isInitMap = false;
}
