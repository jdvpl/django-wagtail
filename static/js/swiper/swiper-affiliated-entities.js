/* update Swiper Items */
let SwiperAffiliatedEntities = undefined;

updateSwiperAffiliatedEntities = () => {
  
  
  try {
    if (SwiperAffiliatedEntities != undefined) {
      SwiperAffiliatedEntities.destroy(true, true);
    }
  } catch (error) {
    //console.error(error);
  }

  SwiperAffiliatedEntities = new Swiper(".sector-company", {
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
      nextEl: ".sector-company-next",
      prevEl: ".sector-company-prev",
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
  updateSwiperAffiliatedEntities();
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
