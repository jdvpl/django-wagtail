/* update Swiper Items */
let SwiperRelatedCompanyMobil = undefined;

updateSwiperRelatedCompanyMobil = () => {
  try {
    if (SwiperRelatedCompanyMobil != undefined) {
      SwiperRelatedCompanyMobil.destroy(true, true);
    }
  } catch (error) {
    //console.error(error);
  }

  SwiperRelatedCompanyMobil = new Swiper(".related-company-mobil", {
    loop: true,
    clickable: true,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 5000,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".related-company-mobil-next",
      prevEl: ".related-company-mobil-prev",
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 5,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 5,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 10,
      },
      1366: {
        slidesPerView: 4,
        spaceBetween: 10,
      },
    },
  });
};
/* update Swiper Items */

/* Swiper Init */
document.addEventListener("DOMContentLoaded", function () {
  updateSwiperRelatedCompanyMobil();
});
/* Swiper Init */

/* Swiper Events */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".swiper-slide").forEach(function (element) {
    element.addEventListener("click", function (e) {
      document.querySelectorAll(".swiper-slide").forEach(function (element) {
        element.classList.remove("active");
      });
      element.classList.add("active");
      document.querySelectorAll(".swiper-tab").forEach(function (element) {
        element.classList.remove("active");
        element.classList.remove("show");
      });
      let target = document.getElementById(element.dataset.bsTarget);
      target.classList.add("active");
      target.classList.add("show");
    });
  });
});
/* Swiper Events */
