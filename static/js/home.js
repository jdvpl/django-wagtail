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
