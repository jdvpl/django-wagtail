/**
 * Metodo que permite visualizar la caja de un item
 * y oculta los items relacionados por clase.
 * @param string itemID ID del item seleccionado
 * @param string className Nombre de la clase de los 
 *      objetos relacionados
 * @see estructura_sector.html
 * @see cultura_corporativa_page.html 
 * @see mme-raw.css 
 */
function showItem(itemID, className) {
    // Obtiene los elementos y los oculta
    let item = document.getElementById(itemID);
    let itemObjArr = document.getElementsByClassName(className);
    Array.prototype.forEach.call(itemObjArr, function(itemObj) {
        if (hasClass(itemObj, 'show-elemen')) {
            itemObj.classList.add('hide-element');
        }
    });
    // Muestra solo la caja de texto del elemento 
    // seleccionado
    item.classList.remove('hide-element');
    item.classList.add('show-elemen');
}

/**
 * Metodo que permite visualizar la seleccion de un boton
 * de contenido de objetivos.
 * @param string itemID ID del item seleccionado
 * @param string className Nombre de la clase de los 
 *      objetos relacionados
 * @see cultura_corporativa_page.html 
 */
 function setActiveItem(itemID, className) {
    // Obtiene los elementos y los desactiva
    let item = document.getElementById(itemID);
    let itemObjArr = document.getElementsByClassName(className);
    Array.prototype.forEach.call(itemObjArr, function(itemObj) {
        if (hasClass(itemObj, 'active')) {
            itemObj.classList.remove('active');
        }
    });
    // Activa el elemento seleccionado
    item.classList.add('active');
}

/**
 * Metodo que permite visualizar la seleccion de un boton
 * de estructra del sector.
 * @param string className Nombre de la clase del elemento
 *               seleccionado.
 * @see estructura_sector.html 
 */
function setSelectedItem(itemImg, className) {
    // Obtiene los elementos y los desactiva
    let item = document.getElementsByClassName(className);
    let itemObjArr = document.getElementsByClassName('bt-box');
    let itemImgArr = document.getElementsByClassName('btn-effect');
    Array.prototype.forEach.call(itemObjArr, function(itemObj) {
        if (hasClass(itemObj, 'active-item')) {
            itemObj.classList.remove('active-item');
        }
    });
    Array.prototype.forEach.call(itemImgArr, function(itImg) {
        if (hasClass(itImg, 'active-img')) {
            itImg.classList.remove('active-img');
        }
    });
    // Activa el elemento seleccionado
    item[0].classList.add('active-item');
    itemImg = itemImg.getElementsByClassName('btn-effect');
    itemImg[0].classList.add('active-img');
}

/**
 * Para el caso de Movil 2 mueve el elemento.
 * @param string clsBox Clase de elemento contenedor. 
 * @param string itemID de elemento a mover.
 * @see estructura_sector.html
 */
function moveMB(clsBox, itemID) {
    if (window.innerWidth < 480) {
        let item = document.getElementById(itemID);
        let box = document.getElementsByClassName(clsBox)[0];
        box.parentNode.insertBefore(item, box);
    }
}

/**
 * Controla la visualizacion del componente de vison
 * mision y proposito
 * @param {*} itemID 
 * @param {*} className 
 * @param {*} imageID
 * @see cultura_corporativa.html 
 */
function showItemSpan(itemID, iclassName, sclassName, imageID) {
    let item = document.getElementById(itemID);
    let itemImage = document.getElementById(imageID);
    let itemObjArr = document.getElementsByClassName(iclassName);
    let imageObjArr = document.getElementsByClassName(sclassName);
    // Obtiene los elementos y los oculta
    Array.prototype.forEach.call(itemObjArr, function(itemObj) {
        if (hasClass(itemObj, 'show-elemen')) {
            itemObj.classList.add('hide-element');
        }
    });
    // Muestra todas las imagenes
    Array.prototype.forEach.call(imageObjArr, function(itemObj) {
        if (hasClass(itemObj, 'hide-element')) {
            itemObj.classList.remove('hide-element');
            itemObj.classList.add('show-elemen');
        }
    });
    // Muestra solo la caja de texto del elemento
    // seleccionado
    item.classList.remove('hide-element');
    item.classList.add('show-elemen');
    itemImage.classList.add('hide-element');
}
