$("document").ready(function () {
  for (var i = 0; i < boards.boards.length; i++) {
    data(i);
  }
});

var isMobile = {
  Android: function () {
    return navigator.userAgent.match(/Android/i);
  },
  BlackBerry: function () {
    return navigator.userAgent.match(/BlackBerry/i);
  },
  iOS: function () {
    return navigator.userAgent.match(/iPhone|iPad|iPod/i);
  },
  Opera: function () {
    return navigator.userAgent.match(/Opera Mini/i);
  },
  Windows: function () {
    return (
      navigator.userAgent.match(/IEMobile/i) ||
      navigator.userAgent.match(/WPDesktop/i)
    );
  },
  any: function () {
    return (
      isMobile.Android() ||
      isMobile.BlackBerry() ||
      isMobile.iOS() ||
      isMobile.Opera() ||
      isMobile.Windows()
    );
  },
};

function data(number) {
  // Get the reference to the html element where the report is embedded
  var reportContainer = document.getElementById(boards.boards[number].id);
  // Global variable for the report object
  var report;
  // Get object from models to access embedded configuration
  var models;
  var loadBoard = false;
  var is_desktop = false;
  var is_mobil = false;

  let loadPowerBI = (layout) => {
    //Invoke the API to get the authentication token
    fetch(boards.boards[number].url, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((result) => {
        var embedUrl = result.embedReports[0].embedUrl;
        var accessToken = result.embedToken;

        // Get object from models to access embedded configuration
        models = window["powerbi-client"].models;

        /* Layout Types */
        /* layoutType: models.LayoutType.MobilePortrait, */
        /* layoutType: models.LayoutType.Custom, */
        /* layoutType: models.LayoutType.MobileLandscape, */
        /* Layout Types */
        /* This configuration resolve the fit to width - pageView: "fitToWidth", */

        var config = {
          type: "report",
          embedUrl: embedUrl,
          accessToken: accessToken,
          tokenType: models.TokenType.Embed,
          viewMode: models.ViewMode.View,
          permissions: models.Permissions.Read,
          settings: {
            localeSettings: {
              language: "es",
              formatLocale: "es",
            },
            filterPaneEnabled: false,
            navContentPaneEnabled: true,
            layoutType: isMobile.any()
              ? models.LayoutType.MobilePortrait
              : models.LayoutType.Custom,
            customLayout: {
              displayOption: models.DisplayOption.FitToPage,
            },
          },
        };

        // Embeber el reporte y mostrarlo dentro del contenedor div
        report = powerbi.embed(reportContainer, config);
        /* console.log('report clear')
                powerbi.reset(reportContainer) */

        // Adicionar la variable para hacer trazabilidad del mode actual de presentación
        var viewMode = "view";
        loadBoard = true;
      })
      .catch((error) =>
        console.error(
          "Un error ha ocurrido al cargar el reporte. Detalle : " + error
        )
      );
  };
  loadPowerBI(PBIWindowSize());
  function PBIWindowSize() {
    if (window.innerWidth > 1000) {
      is_desktop = true;
      is_mobile = false;
      return false;
    } else {
      is_desktop = false;
      is_mobile = true;
      return true;
    }
  }
  /**
   * Function to resize the reportContainer div to the size of the user's browser window
   */
  function reportWindowSize() {
    var widthBuffer = 40;
    /* We need define the best way to calculate the board height */
    var heightBuffer = (window.innerHeight / 3) * 2;
    reportContainer.style.height = heightBuffer + "px";
    if (loadBoard) {
      if (window.innerWidth < 1000 && is_mobile == false) {
        is_desktop = false;
        is_mobile = true;
        loadBoard = false;
        powerbi.reset(reportContainer);
        loadPowerBI(true);
      } else if (window.innerWidth > 1000 && is_desktop == false) {
        is_desktop = true;
        is_mobile = false;
        loadBoard = false;
        powerbi.reset(reportContainer);
        loadPowerBI(false);
      }
    }
  }

  window.onresize = reportWindowSize;
  window.onload = reportWindowSize;
}
