/* update Swiper Items */
let SwiperRelatedCompany = undefined;

updateSwiperRelatedCompany = () => {
  try {
    if (SwiperRelatedCompany != undefined) {
      SwiperRelatedCompany.destroy(true, true);
    }
  } catch (error) {
    //console.error(error);
  }

  SwiperRelatedCompany = new Swiper(".related-company", {
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
      nextEl: ".related-company-next",
      prevEl: ".related-company-prev",
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
  updateSwiperRelatedCompany();
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
