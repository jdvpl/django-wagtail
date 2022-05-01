/* update Swiper Items */
updateSwiperItems = () => {
  
  new Swiper(".mme-swiper", {
    
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
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 5
        },
        768: {
            slidesPerView: 1,
            spaceBetween: 5
        },
        1024: {
            slidesPerView: 2,
            spaceBetween: 10
        },
        1366: {
            slidesPerView: 3,
            spaceBetween: 10
        }
    }
  });
};
/* update Swiper Items */

/* Swiper Init */

document.addEventListener("DOMContentLoaded", function () {
  updateSwiperItems();
});
/* Swiper Init */
