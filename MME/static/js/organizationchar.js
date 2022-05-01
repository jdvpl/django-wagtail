function drawCanvasMovil() {
  var canvas_movil = document.getElementById("canvas-movil");
  var c_movil_width = canvas_movil.scrollWidth;
  var c_movil_height = canvas_movil.scrollHeight;
  document.getElementById("minister-movil").style["left"] =
    c_movil_width / 2 - 125 + "px";
  document.getElementById("fun-movil-1").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-2").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-3").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-4").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-5").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-6").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-7").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-8").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-9").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-10").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-11").style["left"] =
    c_movil_width / 2 - 65 + "px";
  document.getElementById("fun-movil-12").style["left"] =
    c_movil_width / 2 - 65 + "px";
  if (canvas_movil.getContext) {
    var ctx = canvas_movil.getContext("2d");
    ctx.beginPath();
    ctx.lineWidth = 4;
    ctx.strokeStyle = "#d9d9d9";

    var intervals = (c_movil_height - 800) / 12;

    /* minister tree */
    /* center */
    ctx.beginPath();
    ctx.moveTo(c_movil_width / 2, 420);
    ctx.lineTo(c_movil_width / 2, 490);
    ctx.stroke();
    /* center */
    /* horizontal */
    ctx.beginPath();
    ctx.moveTo(c_movil_width / 2 + 2, 490);
    ctx.lineTo(50, 490);
    ctx.stroke();
    /* horizontal */

    var divider = 600;
    for (let index = 0; index < 12; index++) {
      /* horizontal */
      ctx.beginPath();
      ctx.moveTo(c_movil_width / 2, divider);
      ctx.lineTo(50, divider);
      ctx.stroke();
      /* horizontal */
      divider = divider + 330;
    }

    /* vertical */
    ctx.beginPath();
    ctx.moveTo(50, 488);
    ctx.lineTo(50, divider - 330 + 2);
    ctx.stroke();
    /* vartical */

    /* minister tree */
  }
}

function drawCanvasTablet() {
  var canvas_tablet = document.getElementById("canvas-tablet");
  var c_tablet_width = canvas_tablet.scrollWidth;
  var c_tablet_height = canvas_tablet.scrollHeight;
  document.getElementById("minister-tablet").style["left"] =
    c_tablet_width / 2 - 100 + "px";
  document.getElementById("general-secretary-tablet").style["left"] =
    c_tablet_width - 200 + "px";
  if (canvas_tablet.getContext) {
    var ctx = canvas_tablet.getContext("2d");

    var intervals = (c_tablet_height - 800) / 9;

    ctx.beginPath();
    ctx.lineWidth = 4;
    ctx.strokeStyle = "#d9d9d9";
    ctx.lineJoin = "round";

    /* viceminister-mines */
    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(220, 100);
    ctx.lineTo(c_tablet_width / 2 - 50, 255);
    ctx.stroke();
    /* viceminister-mines */

    /* viceminister-energy */
    ctx.beginPath();
    ctx.moveTo(100, 550);
    ctx.lineTo(220, 550);
    ctx.lineTo(c_tablet_width / 2 - 50, 375);
    ctx.stroke();
    /* viceminister-energy */

    /* general-secretary */
    ctx.beginPath();
    ctx.moveTo(c_tablet_width / 2, 340);
    ctx.lineTo(c_tablet_width - 100, 340);
    ctx.stroke();
    /* general-secretary */

    /* minister tree */
    /* center */
    ctx.beginPath();
    ctx.moveTo(c_tablet_width / 2, 560);
    ctx.lineTo(c_tablet_width / 2, 750);
    ctx.stroke();
    /* center */
    /* horizontal */
    ctx.beginPath();
    ctx.moveTo(c_tablet_width / 2 + 2, 750);
    ctx.lineTo(70, 750);
    ctx.stroke();
    /* horizontal */

    var divider = 880;
    var normal = false;
    var line_length = 0;
    for (let index = 0; index < 9; index++) {
      /* horizontal */

      if (index % 2 == 0) {
        line_length = c_tablet_width / 4;
      } else {
        line_length = c_tablet_width / 2;
      }

      ctx.beginPath();
      ctx.moveTo(line_length + 10, divider);
      ctx.lineTo(72, divider);
      ctx.stroke();
      /* horizontal */
      divider = divider + 165;
    }

    /* vertical */
    ctx.beginPath();
    ctx.moveTo(72, 750);
    ctx.lineTo(72, divider - 164);
    ctx.stroke();
    /* vartical */

    /* minister tree */
  }
}

function drawCanvasDesktop() {
  var OCDesktop1400 = document.getElementById("canvas-desktop");
  var OCDesktop = document.getElementById("desktop-chart");
  var c_desktop_width = OCDesktop.offsetWidth;
  var c_desktop_height = OCDesktop1400.scrollHeight;
  document.getElementById("minister-desktop").style["left"] =
    c_desktop_width / 2 - 120 + "px";
  if (OCDesktop1400.getContext) {
    var ctx_1366 = OCDesktop1400.getContext("2d");

    ctx_1366.beginPath();
    ctx_1366.lineWidth = 4;
    ctx_1366.strokeStyle = "#d9d9d9";
    ctx_1366.lineJoin = "round";

    /* viceminister-mines */
    ctx_1366.beginPath();
    ctx_1366.moveTo(200, 160);
    ctx_1366.lineTo(410, 160);
    ctx_1366.lineTo(c_desktop_width / 2, 260);
    ctx_1366.stroke();
    /* viceminister-mines */

    /* viceminister-energy */
    ctx_1366.beginPath();
    ctx_1366.moveTo(200, 380);
    ctx_1366.lineTo(410, 380);
    ctx_1366.lineTo(c_desktop_width / 2, 300);
    ctx_1366.stroke();
    /* viceminister-energy */

    /* general-secretary */
    ctx_1366.beginPath();
    ctx_1366.moveTo(c_desktop_width / 2, 280);
    ctx_1366.lineTo(c_desktop_width - 200, 280);
    ctx_1366.stroke();
    /* general-secretary */

    /* minister tree */
    /* center */
    ctx_1366.beginPath();
    ctx_1366.moveTo(c_desktop_width / 2, 500);
    ctx_1366.lineTo(c_desktop_width / 2, 620);
    ctx_1366.stroke();
    document.getElementById(
      "office-environmental-social-affairs-desktop"
    ).style["left"] = c_desktop_width / 2 - 90 + "px";
    /* center */
    /* horizontal */
    ctx_1366.beginPath();
    ctx_1366.moveTo(c_desktop_width / 2 - 497, 550);
    ctx_1366.lineTo(c_desktop_width / 2 + 497, 550);
    ctx_1366.stroke();
    /* horizontal */

    /* vertical*/
    var div = c_desktop_width / 2 - 123.75;
    document.getElementById("legislative-affairs-group-desktop").style["left"] =
      div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 930);
    ctx_1366.stroke();
    div = c_desktop_width / 2 - 123.75 * 2;

    document.getElementById("strategic-management-group-desktop").style[
      "left"
    ] = div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 620);
    ctx_1366.stroke();
    div = c_desktop_width / 2 - 123.75 * 3;

    document.getElementById("communication-press-group").style["left"] =
      div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 930);
    ctx_1366.stroke();
    div = c_desktop_width / 2 - 123.75 * 4;

    document.getElementById("results-unit-group-desktop").style["left"] =
      div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 620);
    ctx_1366.stroke();

    div = c_desktop_width / 2 + 123.75;
    document.getElementById("office-regulatory-business-affairs-desktop").style[
      "left"
    ] = div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 930);
    ctx_1366.stroke();

    div = c_desktop_width / 2 + 123.75 * 2;
    document.getElementById("legal-advisory-office-desktop").style["left"] =
      div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 620);
    ctx_1366.stroke();

    div = c_desktop_width / 2 + 123.75 * 3;
    document.getElementById("internal-control-office-desktop").style["left"] =
      div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 930);
    ctx_1366.stroke();

    div = c_desktop_width / 2 + 123.75 * 4;
    document.getElementById(
      "international-planning-management-office-desktop"
    ).style["left"] = div - 90 + "px";
    ctx_1366.beginPath();
    ctx_1366.moveTo(div, 550);
    ctx_1366.lineTo(div, 620);
    ctx_1366.stroke();
    /* vertical*/

    /* minister tree */
  }
}

function reportWindowSize() {
  /* txt = document.getElementById("ancho");
        txt.innerHTML = " outer "+window.outerWidth +" inner "+window.innerWidth; */
  if (window.outerWidth >= 1300) {
    document.getElementById("desktop-chart").style.display = "block";
    document.getElementById("movil-chart").style.display = "none";
    document.getElementById("tablet-chart").style.display = "none";

    var canvas = document.getElementById("canvas-desktop");
    canvas.width = document.getElementById("desktop-chart").offsetWidth;

    drawCanvasDesktop();
  }
  if (window.outerWidth >= 768 && window.outerWidth < 1299) {
    document.getElementById("desktop-chart").style.display = "none";
    document.getElementById("movil-chart").style.display = "none";
    document.getElementById("tablet-chart").style.display = "block";

    var canvas = document.getElementById("canvas-tablet");
    canvas.width = document.getElementById("tablet-chart").offsetWidth;
    drawCanvasTablet();
  }
  if (window.outerWidth < 768) {
    document.getElementById("desktop-chart").style.display = "none";
    document.getElementById("tablet-chart").style.display = "none";
    document.getElementById("movil-chart").style.display = "block";

    var canvas = document.getElementById("canvas-movil");
    canvas.width = document.getElementById("movil-chart").offsetWidth;
    drawCanvasMovil();
  }
}

window.onresize = reportWindowSize;
window.onload = reportWindowSize;

const $boton = document.querySelector("#btnCapturar"),
  $objetivo = document.body;

$boton.addEventListener("click", () => {
  html2canvas($objetivo).then((canvas) => {
    let dw_link = document.createElement("a");
    dw_link.download = "Organigrama Ministerio de Minas y Energía.png";
    dw_link.href = canvas.toDataURL();
    dw_link.click();
  });
});
