/* icon-menu-mme Events */
document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelectorAll(".icon-menu-mme-option")
    .forEach(function (element) {
      element.addEventListener("click", function (e) {
        document
          .querySelectorAll(".icon-menu-mme-option")
          .forEach(function (element) {
            element.classList.remove("active");
          });
        element.classList.add("active");
        
        document
          .querySelectorAll(".icon-menu-mme-option-content")
          .forEach(function (element) {
            element.classList.remove("active");
          });

        let target = null;

        target = document.getElementById(element.dataset.bsTarget);
        target.classList.add("active");

        target = document.getElementById(element.dataset.bsTarget + "-mobil");
        target.classList.add("active");

      });
    });
});
/* icon-menu-mme Events */
