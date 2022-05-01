//--------------------------------------------------------
// Variables globales
//--------------------------------------------------------

/**
 * Referencia al objeto del slider principal.
 */
var mainSwiper = null;

//--------------------------------------------------------
// Funcion Principal
//--------------------------------------------------------

/**
 * Funcion principal de cargue.
 */
(function() {
    mainSwiper = new Swiper('#carouselPrincipal', {
        loop: true,
        effect: 'fade',
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        }
    });
})();
