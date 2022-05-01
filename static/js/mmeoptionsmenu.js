/* MME menu options Events */
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".mme-menu-option").forEach(function (element) {
      element.addEventListener("click", function (e) {
        document.querySelectorAll(".mme-menu-option").forEach(function (element) {
          element.classList.remove("active");
        });
        element.classList.add("active");
  
        document
          .querySelectorAll(".mme-menu-content-item")
          .forEach(function (element) {
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
/* MME menu options Events */
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".mme-menu-option2").forEach(function (element) {
      element.addEventListener("click", function (e) {
        document.querySelectorAll(".mme-menu-option2").forEach(function (element) {
          element.classList.remove("active2");
        });
        element.classList.add("active2");
  
        document
          .querySelectorAll(".mme-menu-content-item2")
          .forEach(function (element) {
            element.classList.remove("active2");
          });
        let target = null;
  
        target = document.getElementById(element.dataset.bsTarget);
        target.classList.add("active2");
  
        target = document.getElementById("movil" + element.dataset.bsTarget);
        target.classList.add("active2");
      });
    });
  });
  /* MME menu options Events */
  