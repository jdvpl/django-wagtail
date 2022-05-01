/* Social networks Events */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".network-item").forEach(function (element) {
    element.addEventListener("click", function (e) {
      document.querySelectorAll(".network-item").forEach(function (element) {
        element.classList.remove("active");
      });
      element.classList.add("active");

      document.querySelectorAll(".content-network").forEach(function (element) {
        element.classList.remove("active");
      });
      let target = null;

      target = document.getElementById(element.dataset.bsTarget);
      target.classList.add("active");

      target = document.getElementById("movil" + element.dataset.bsTarget);
      target.classList.add("active");
    });
  });
});
/* Social networks Events */
