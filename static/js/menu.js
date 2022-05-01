/**
 * Marca la pagina actual.
 * 
 * @param string page Pagina actual 
 */
function setMain(page) {

}

/**
 * On load del dom.
 */
(function() {
    // Configura la versiones tableta y celular
    document.addEventListener("DOMContentLoaded", function(){
        if (window.innerWidth <= 768) {    
            document.querySelectorAll('.navbar .dropdown').forEach(function(everydropdown){
                everydropdown.addEventListener('hidden.bs.dropdown', function () {
                    this.querySelectorAll('.submenu').forEach(function(everysubmenu){
                        everysubmenu.style.display = 'none';
                    });
                })
            });
            document.querySelectorAll('.dropdown').forEach(function(element) {
                if(element.classList.contains('nav-item-separator')) {
                    console.log(element);
                    element.addEventListener('click', function (e) {
                        if (element !== e.target) return;
                        let itemObjArr = this.querySelectorAll('ul');
                        Array.prototype.forEach.call(itemObjArr, function(nextEl) {
                            if(nextEl && nextEl.classList.contains('dropdown-menu')) {	
                                e.preventDefault();
                                if(nextEl.style.display == 'block'){
                                    nextEl.style.display = 'none';
                                } else {
                                    nextEl.style.display = 'block';
                                }   
                            }
                        });
                    });
                }
            });
        }
    });
})();
