// DOMContentLoaded
// Main menu

dataTargetDevice = () => {
  document.querySelectorAll(".menu-title").forEach(function (element) {
    if (window.innerWidth > 1199) {
      element.dataset.bsToggle = "desktop";
    } else {
      element.dataset.bsToggle = "dropdown";
    }
  });
};

closeActiveDropdowns = (current) => {
  document.querySelectorAll(".dropdown-menu a").forEach(function (element) {
    if (element != current) {
      element.classList.remove("open");
      let nextEl = element.nextElementSibling;
      if (nextEl && nextEl.classList.contains("submenu")) {
        // Hide block
        if (nextEl.style.display == "block") {
          nextEl.style.display = "none";
        }
      }
    }
  });
};

updateWindowsDisplay = () => {
  /////// Prevent closing from click inside dropdown
  document.querySelectorAll(".dropdown-menu").forEach(function (element) {
    element.addEventListener("click", function (e) {
      e.stopPropagation();
    });
  });

  // make it as accordion for smaller screens
  if (window.innerWidth < 1200) {
    // close all inner dropdowns when parent is closed
    document
      .querySelectorAll(".navbar .dropdown")
      .forEach(function (everydropdown) {
        everydropdown.addEventListener("hidden.bs.dropdown", function () {
          // after dropdown is hidden, then find all submenus
          this.querySelectorAll(".submenu").forEach(function (everysubmenu) {
            // hide every submenu as well
            everysubmenu.style.display = "none";
          });
        });
      });

    document.querySelectorAll(".dropdown-menu a").forEach(function (element) {
      element.addEventListener("click", function (e) {
        closeActiveDropdowns(element);
        element.classList.toggle("open");
        let nextEl = this.nextElementSibling;
        if (nextEl && nextEl.classList.contains("submenu")) {
          // prevent opening link if link needs to open dropdown
          e.preventDefault();
          if (nextEl.style.display == "block") {
            nextEl.style.display = "none";
          } else {
            nextEl.style.display = "block";
          }
        }
      });
    });
  }
  // end if innerWidth
};

document.addEventListener("DOMContentLoaded", function () {
  dataTargetDevice();
  updateWindowsDisplay();
});
// Main menu
// DOMContentLoaded  end

reportWindowSize = () => {
  dataTargetDevice();
  updateWindowsDisplay();
};

window.onresize = reportWindowSize;
