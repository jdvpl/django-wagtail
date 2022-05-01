
let swiperobjects = [];

destroySwiper = (sw) => {
  if (sw != undefined && sw.length==1) {
    sw.destroy(true, true);
  }
};

createSwiper = (index) => {
  var mmeswiper;
  mmeswiper = new Swiper(".mme-swiper-" + index, {
    slidesPerView: 1,
    spaceBetween: 10,
    /* slidesPerGroup: 3, */
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
      nextEl: ".btn-next-" + index,
      prevEl: ".btn-prev-" + index,
    },
  });
  return mmeswiper;
};

updateSwiperItems = () => {
  for (var i = 0; i < swiperobjects.length; i++) {
    destroySwiper(swiperobjects[i]);
  }
  swiperobjects = [];

  document
    .querySelectorAll(".swiper-container-mme")
    .forEach(function (element, index) {
      swiperobjects.push(createSwiper(index));
    });
};
/* update Swiper Items */

/* Swiper Init */

document.addEventListener("DOMContentLoaded", function () {
  updateSwiperItems();
});
/* Swiper Init */
