//--------------------------------------------------------
// Variables globales
//--------------------------------------------------------

var entitySwiper = null;

//--------------------------------------------------------
// Funciones de manejadores de eventos
//--------------------------------------------------------

/**
 * Remueve la caracteristica de imagen gris
 * @param {} imgObj Tag img de la entidad
 * @see entities_block.html
 */
function onmouseoverHandlerSE(imgObj) {
    imgObj.classList.remove('gray-img');
}

/**
 * Adiciona la caracteristica de imagen gris
 * @param {} imgObj Tag img de la entidad
 * @see entities_block.html
 */
function onmouseoutHandlerSE(imgObj) {
    if (!hasClass(imgObj, 'active-entity')) {
        imgObj.classList.add('gray-img');
    }
}

/**
 * Adiciona la caracteristica de imagen activada
 * @param {} imgObj Tag img de la entidad
 * @see entities_block.html
 */
 function setActiveEntity(imgObj) {
    let imgObjArr = document.getElementsByClassName('img-entity');
    // Oculta los elementos 
    Array.prototype.forEach.call(imgObjArr, function(imgOj) {
        if (hasClass(imgOj, 'active-entity')) {
            imgOj.classList.add('gray-img');
            imgOj.classList.remove('active-entity');
        }
    });
    imgObj.classList.remove('gray-img');
    imgObj.classList.add('active-entity');
}

/**
 * Permite mostrar la descripcion de la enidad
 * seleccionada
 * @param string infoID ID de la caja de texto
 * @see affilated_entities_block.html
 */
function showInfo(infoID) {
    // Obtiene el elemento y los elementos relacionados
    let infObj = document.getElementById(infoID);
    let infoObjArr = document.getElementsByClassName('entity-info');
    // Oculta los elementos 
    Array.prototype.forEach.call(infoObjArr, function(infoObj) {
        if (hasClass(infoObj, 'show-elemen')) {
            infoObj.classList.add('hide-element');
        }
    });
    // Hace visible el elementom a mostrar
    infObj.classList.remove('hide-element');
    infObj.classList.add('show-elemen');
}

/**
 * Carga el slider de entidades.
 * @see estructura_sector.html
 */
function loadEntitySwiper() {
    const winMax = 768;
    const winMin = 320;
    // Limpia la memoria
    if (entitySwiper) {
        Array.prototype.forEach.call(entitySwiper, function(entity) {
            entity.destroy();
        });
        entitySwiper = null;
    }
    // Genera la instancia
    entitySwiper = new Swiper('.carouselEntity', {
        loop: true,
        slidesPerView: 5,
        spaceBetween: 10,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 5
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 5
            },
            1024: {
                slidesPerView: 3,
                spaceBetween: 10
            },
            1366: {
                slidesPerView: 5,
                spaceBetween: 10
            }
        }
    });
}

//--------------------------------------------------------
// Funcion Principal
//--------------------------------------------------------

(function() {
    loadEntitySwiper();    
})();
